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

    def __init__(self, dim, num_heads, dropout_p):
        super().__init__()
        self.q = torch.nn.Linear(dim, dim)
        self.k = torch.nn.Linear(dim, dim)
        self.v = torch.nn.Linear(dim, dim)
        self.dropout = torch.nn.Dropout(dropout_p)
        self.softmax = torch.nn.Softmax(dim=(- 1))

    def forward(self, query, key, value, scale_factor=1):
        q = self.q(query)
        k = self.k(key)
        v = self.v(value)
        q = torch.transpose(q, (- 2), (- 1))
        k = torch.transpose(k, (- 2), (- 1))
        qk = torch.matmul(q, k)
        scaled_qk = (qk * scale_factor)
        softmax_qkl = self.softmax(scaled_qk)
        dropout_qkl = self.dropout(softmax_qkl)
        output = torch.matmul(dropout_qkl, v)
        output = torch.transpose(output, (- 2), (- 1))
        return output



dim = 1
num_heads = 1
dropout_p = 1

func = Model(dim, num_heads, dropout_p).to('cuda')



x1 = torch.randn(1, 50, 512)



x2 = torch.randn(1, 60, 512)



x3 = torch.randn(1, 60, 512)

query = 1

test_inputs = [x1, x2, x3, query]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (50x512 and 1x1)

jit:
Failed running call_module L__self___q(*(FakeTensor(..., device='cuda:0', size=(1, 50, 512)),), **{}):
a and b must have same reduction dim, but got [50, 512] X [1, 1].

from user code:
   File "<string>", line 26, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''