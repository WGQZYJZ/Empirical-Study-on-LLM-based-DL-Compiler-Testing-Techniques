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

    def __init__(self, attention_hidden_size, num_attention_heads, dropout_p):
        super().__init__()
        self.dropout = torch.nn.Dropout(dropout_p)
        self.softmax = torch.nn.Softmax()

    def forward(self, query, key, value, scale_factor=None, dropout_p=None):
        qk = torch.matmul(query, key.transpose((- 2), (- 1)))
        scaled_qk = (qk / scale_factor)
        softmax_qk = self.softmax(scaled_qk, dim=(- 1))
        dropout_qk = self.dropout(softmax_qk)
        output = dropout_qk.matmul(value)
        return output



attention_hidden_size = 1
num_attention_heads = 1
dropout_p = 1

func = Model(attention_hidden_size, num_attention_heads, dropout_p).to('cuda')



query = torch.randn(15, 4, 512)



key = torch.randn(16, 4, 512)



value = torch.randn(16, 4, 512)


test_inputs = [query, key, value]

# JIT_FAIL
'''
direct:
The size of tensor a (15) must match the size of tensor b (16) at non-singleton dimension 0

jit:
Failed running call_function <built-in method matmul of type object at 0x74127e2699e0>(*(FakeTensor(..., device='cuda:0', size=(15, 4, 512)), FakeTensor(..., device='cuda:0', size=(16, 512, 4))), **{}):
Shape mismatch: objects cannot be broadcast to a single shape

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''