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

    def __init__(self, dim, num_heads, num_qk, num_v, dropout_p):
        super().__init__()
        self.qkv = torch.nn.Linear(dim, (num_heads * (num_qk + num_v)))
        self.softmax = torch.nn.Softmax(dim=(- 1))
        self.dropout = torch.nn.Dropout(dropout_p)

    def forward(self, query, key, value, dropout_p):
        qkv = self.qkv(query)
        qkv = torch.chunk(qkv, chunks=2, dim=(- 1))
        (q, k, v) = map((lambda t: torch.transpose(t, 1, 2)), qkv)
        scale_factor = (dim ** (- 0.5))
        qk = torch.matmul(query, key.transpose((- 2), (- 1)))
        scaled_qk = qk.mul(scale_factor)
        softmax_qk = self.softmax(scaled_qk)
        dropout_qk = self.dropout(softmax_qk)
        output = dropout_qk.matmul(value)
        output = torch.transpose(output, 1, 2)
        return output



dim = 1
num_heads = 1
num_qk = 1
num_v = 1

dropout_p = 0.1


func = Model(dim, num_heads, num_qk, num_v, dropout_p).to('cuda')



query = torch.randn(1, 8, 64)



key = torch.randn(1, 16, 64)



value = torch.randn(1, 16, 64)

dropout_p = 1

test_inputs = [query, key, value, dropout_p]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (8x64 and 1x2)

jit:
Failed running call_module L__self___qkv(*(FakeTensor(..., device='cuda:0', size=(1, 8, 64)),), **{}):
a and b must have same reduction dim, but got [8, 64] X [1, 2].

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''