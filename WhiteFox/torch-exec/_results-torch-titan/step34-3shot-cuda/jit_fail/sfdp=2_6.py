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

    def __init__(self, seq_len: int=32, query_feature: int=8, key_feature: int=16):
        super().__init__()
        self.query = torch.nn.Parameter(torch.randn(1, seq_len, query_feature))
        self.key = torch.nn.Parameter(torch.randn(1, seq_len, key_feature))
        self.inv_scale_factor = torch.nn.Parameter(torch.randn(1))
        self.dropout = torch.nn.Dropout(0.1)

    def forward(self, value, dropout_p_):
        qk = torch.matmul(self.query, self.key.transpose((- 2), (- 1)))
        scaled_qk = qk.div(self.inv_scale_factor)
        softmax_qk = scaled_qk.softmax(dim=(- 1))
        dropout_qk = self.dropout(softmax_qk)
        output = dropout_qk.matmul(value)
        return output



func = Model(seq_len=32, query_feature=8, key_feature=16).to('cuda')

value = 1
dropout_p_ = 1

test_inputs = [value, dropout_p_]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [1, 8] but got: [1, 16].

jit:
Failed running call_function <built-in method matmul of type object at 0x7eadf9c699e0>(*(Parameter(FakeTensor(..., device='cuda:0', size=(1, 32, 8), requires_grad=True)), FakeTensor(..., device='cuda:0', size=(1, 16, 32), requires_grad=True)), **{}):
Expected size for first two dimensions of batch2 tensor to be: [1, 8] but got: [1, 16].

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''