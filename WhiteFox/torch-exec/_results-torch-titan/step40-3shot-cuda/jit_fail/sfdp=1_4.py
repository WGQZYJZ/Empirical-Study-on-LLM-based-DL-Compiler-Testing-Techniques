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

    def __init__(self, dim_query, dim_key, dim_value, num_heads, dropout_p=0.0):
        super().__init__()
        self.scale_factor = (dim_key ** (- 0.5))
        self.linear_q = torch.nn.Linear(dim_query, (dim_key * num_heads), bias=False)
        self.linear_k = torch.nn.Linear(dim_key, (dim_key * num_heads), bias=False)
        self.linear_v = torch.nn.Linear(dim_value, (dim_value * num_heads), bias=False)
        self.dropout = torch.nn.Dropout(dropout_p)

    def forward(self, query, key, value):
        q = self.linear_q(query)
        k = self.linear_k(key)
        v = self.linear_v(value)
        q = q.view((- 1), q.size(1), self.num_heads, k.size((- 1)))
        k = k.view((- 1), self.num_heads, k.size(1), k.size((- 1)))
        v = v.view((- 1), self.num_heads, v.size(1), v.size((- 1)))
        qk = torch.matmul(q, k.transpose((- 2), (- 1)))
        scaled_qk = qk.div(self.scale_factor)
        softmax_qk = scaled_qk.softmax(dim=(- 1))
        dropout_qk = self.dropout(softmax_qk)
        return torch.matmul(dropout_qk, v)



dim_query = 1
dim_key = 1
dim_value = 1
num_heads = 1

func = Model(dim_query, dim_key, dim_value, num_heads).to('cuda')



query = torch.randn(2, 2, 2)



key = torch.randn(2, 3, 3)



value = torch.randn(2, 3, 4)


test_inputs = [query, key, value]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (4x2 and 1x1)

jit:
Failed running call_module L__self___linear_q(*(FakeTensor(..., device='cuda:0', size=(2, 2, 2)),), **{}):
a and b must have same reduction dim, but got [4, 2] X [1, 1].

from user code:
   File "<string>", line 26, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''