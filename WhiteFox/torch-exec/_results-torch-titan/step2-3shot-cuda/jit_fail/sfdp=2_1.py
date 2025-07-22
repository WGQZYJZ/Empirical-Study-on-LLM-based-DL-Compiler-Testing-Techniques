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

    def __init__(self, dropout_p, num_heads, d_key):
        super().__init__()
        self.dropout_p = dropout_p
        self.num_heads = num_heads
        self.d_key = d_key
        self.k = torch.nn.Linear(d_key, d_key, bias=False)
        self.q = torch.nn.Linear(d_key, d_key, bias=False)
        self.v = torch.nn.Linear(d_key, d_key, bias=False)
        self.softmax_d = (- 1)

    def forward(self, x1):
        _shape = list(x1.shape)
        _shape[1] = self.d_key
        _shape = (_shape[1], _shape[0], _shape[2], (_shape[3] // self.num_heads))
        key = self.k(x1).view(*_shape).transpose(0, 1)
        _shape[0] = self.d_key
        _shape = (_shape[1], _shape[0], _shape[2], (_shape[3] // self.num_heads))
        query = self.q(x1).view(*_shape).transpose(0, 1)
        _shape[0] = self.d_key
        _shape = (_shape[1], _shape[0], _shape[2], (_shape[3] // self.num_heads))
        value = self.v(x1).view(*_shape).transpose(0, 1)
        qk = torch.matmul(query, key.transpose((- 2), (- 1)))
        scaled_qk = qk.div(np.sqrt(qk.shape[(- 1)])).softmax(dim=self.softmax_d)
        dropout_qk = torch.nn.functional.dropout(scaled_qk, p=self.dropout_p)
        _shape = list(value.shape)
        _shape[0] = (value.shape[0] * value.shape[1])
        return dropout_qk.matmul(value.view(*_shape))




dropout_p = 0.1


num_heads = 64


d_key = 1024

func = Model(dropout_p, num_heads, d_key).to('cuda')



d_key = 1024


x1 = torch.randn(1, d_key, 64, 64)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (65536x64 and 1024x1024)

jit:
Failed running call_module L__self___k(*(FakeTensor(..., device='cuda:0', size=(1, 1024, 64, 64)),), **{}):
a and b must have same reduction dim, but got [65536, 64] X [1024, 1024].

from user code:
   File "<string>", line 31, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''