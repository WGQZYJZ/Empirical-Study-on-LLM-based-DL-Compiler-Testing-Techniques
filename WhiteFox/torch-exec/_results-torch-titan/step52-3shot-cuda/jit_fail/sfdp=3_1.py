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

    def __init__(self):
        super().__init__()
        self.q_linear = torch.nn.Linear(512, 256)
        self.k_linear = torch.nn.Linear(512, 256)

    def self_attention(self, q, k, v, s, dropout):
        q = self.q_linear(q)
        k = self.k_linear(k)
        n = k.size((- 2))
        qk = torch.matmul(q, k.transpose((- 2), (- 1)))
        scaled_qk = qk.mul(s)
        softmax_qk = scaled_qk.softmax(dim=(- 1))
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout)
        output = dropout_qk.matmul(v)
        return output

    def forward(self, query, key, value, scale_factor, dropout_p):
        v1 = self.self_attention(query, key, value, scale_factor, dropout_p)
        return v1



func = Model().to('cuda')



query = torch.randn(1, 8, 256)



key = torch.randn(1, 8, 256)



value = torch.randn(1, 8, 256)



dropout_p = torch.empty((1,)).uniform_()

scale_factor = 1

test_inputs = [query, key, value, dropout_p, scale_factor]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (8x256 and 512x256)

jit:
Failed running call_module L__self___q_linear(*(FakeTensor(..., device='cuda:0', size=(1, 8, 256)),), **{}):
a and b must have same reduction dim, but got [8, 256] X [512, 256].

from user code:
   File "<string>", line 34, in forward
  File "<string>", line 23, in self_attention


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''