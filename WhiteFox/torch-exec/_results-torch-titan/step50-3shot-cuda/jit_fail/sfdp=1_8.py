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

    def __init__(self, query_dim, key_dim, num_value):
        super().__init__()
        self.query_proj = torch.nn.Sequential(torch.nn.Linear(query_dim, key_dim))
        self.key_proj = torch.nn.Sequential(torch.nn.Linear(query_dim, key_dim))
        self.inv_scalar = torch.div(1, math.sqrt(query_dim))
        self.dropout = torch.nn.Dropout(p=0.5)
        self.value_proj = torch.nn.Sequential(torch.nn.Linear(query_dim, (query_dim * num_value)))

    def forward(self, query, key, value):
        q = self.query_proj(query)
        k = self.key_proj(key)
        scaled_qk = (torch.matmul(q, k.transpose((- 2), (- 1))) * self.inv_scalar)
        softmax_qk = F.softmax(scaled_qk, dim=(- 1))
        dropout_qk = self.dropout(softmax_qk)
        return torch.matmul(dropout_qk, self.value_proj(value).view(query.size(0), query.size(1), (- 1)))



query_dim = 1
key_dim = 1
num_value = 1
func = Model(8, 4, 10).to('cuda')



query = torch.randn(1, 8)



key = torch.randn(10, 4)



value = torch.randn(10, 8)


test_inputs = [query, key, value]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (10x4 and 8x4)

jit:
Failed running call_module L__self___key_proj_0(*(FakeTensor(..., device='cuda:0', size=(10, 4)),), **{}):
a and b must have same reduction dim, but got [10, 4] X [8, 4].

from user code:
   File "<string>", line 27, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''