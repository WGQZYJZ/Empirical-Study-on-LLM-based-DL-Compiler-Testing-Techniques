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

    def __init__(self, in_dim, heads_num, mlp_dim):
        super().__init__()
        self.q = torch.nn.Linear(in_dim, in_dim)
        self.k = torch.nn.Linear(in_dim, in_dim)
        self.v = torch.nn.Linear(in_dim, in_dim)
        self.dropout = nn.Dropout()

    def forward(self, query, key, value, scale_factor, dropout_p, mask):
        q = self.q(query)
        k = self.k(key)
        v = self.v(value)
        qk = (torch.matmul(q, k.t()) / scale_factor)
        scaled_qk = qk.softmax()
        dropout_qk = self.dropout(scaled_qk)
        output = dropout_qk.matmul(v)
        return output



in_dim = 1
heads_num = 1
mlp_dim = 1
func = Model(64, 1, 128).to('cuda')



query = torch.randn(1, 8, 64)



key = torch.randn(1, 8, 64)



value = torch.randn(1, 8, 64)



mask = torch.randn(1, 1, 8)

scale_factor = 1
dropout_p = 1

test_inputs = [query, key, value, mask, scale_factor, dropout_p]

# JIT_FAIL
'''
direct:
t() expects a tensor with <= 2 dimensions, but self is 3D

jit:
Failed running call_method t(*(FakeTensor(..., device='cuda:0', size=(1, 8, 64)),), **{}):
t() expects a tensor with <= 2 dimensions, but self is 3D

from user code:
   File "<string>", line 28, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''