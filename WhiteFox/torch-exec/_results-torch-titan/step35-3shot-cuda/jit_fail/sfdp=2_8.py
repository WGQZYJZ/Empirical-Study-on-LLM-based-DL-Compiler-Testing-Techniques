import os
import torch
import torch.nn.functional as F
import torch.nn as nn
import numpy as np
from torch.autograd import Variable
import math
import torch as th
import torch.linalg as la
from torch.nn import Parameter
import torch.linalg as linalg



class Model(torch.nn.Module):

    def __init__(self, input_channels, key_channels, value_channels, num_heads, dropout_p=0.1):
        super().__init__()
        self.num_heads = num_heads
        self.dropout_p = dropout_p
        self.qk = torch.nn.Conv1d(input_channels, key_channels, kernel_size=1, bias=True)
        self.v = torch.nn.Conv1d(input_channels, value_channels, kernel_size=1, bias=True)

    def forward(self, x):
        qk = self.qk(x)
        value = self.v(x)
        qk_per_head = qk.reshape(((- 1), self.num_heads, (self.key_channels // self.num_heads), x.shape[2]))
        value_per_head = value.reshape(((- 1), self.num_heads, (self.value_channels // self.num_heads), x.shape[2]))
        qk_per_head = qk_per_head.transpose(1, 2)
        scaled_qk = torch.matmul(qk_per_head, value_per_head.transpose((- 2), (- 1)))
        scaled_qk = scaled_qk.div((self.key_channels // (self.num_heads ** 0.5)))
        softmax_qk = scaled_qk.softmax(dim=(- 1))
        if self.training:
            dropout_qk = torch.nn.functional.dropout(softmax_qk, self.dropout_p)
        else:
            dropout_qk = softmax_qk
        dropout_qk = dropout_qk.transpose(1, 2)
        output = dropown_qk.matmul(value_per_head)
        output = output.reshape(((- 1), self.input_channels, x.shape[2]))
        return output



input_channels = 1
key_channels = 1
value_channels = 1
num_heads = 1
func = Model(3, 2, 4, 2).to('cuda')



x = torch.randn(1, 3, 50)


test_inputs = [x]

# JIT_FAIL
'''
direct:
'Model' object has no attribute 'key_channels'

jit:
key_channels

from user code:
   File "<string>", line 27, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''