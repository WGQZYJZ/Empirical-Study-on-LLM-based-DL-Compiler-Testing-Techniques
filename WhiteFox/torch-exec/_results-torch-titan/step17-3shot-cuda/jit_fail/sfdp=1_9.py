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

    def __init__(self, dim, dropout_p):
        super().__init__()
        self.q = torch.nn.Linear(dim, dim)
        self.k = torch.nn.Linear(dim, dim)
        self.inv_scale_factor = nn.Parameter(torch.tensor(1.0))
        self.dropout_p = dropout_p

    def forward(self, query, key, value):
        q = self.q(query)
        k = self.k(key)
        v = value.transpose((- 2), (- 1))
        qk = torch.matmul(q, k)
        scaled_qk = qk.div(self.inv_scale_factor)
        softmax_qk = scaled_qk.softmax(dim=(- 1))
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=self.dropout_p)
        output = dropout_qk.matmul(v)
        return output



dim = 1
dropout_p = 1
func = Model(dim, dropout_p).to('cuda')



query = torch.randn(1, 8, 64, 64)



key = torch.randn(1, 8, 128, 128)



value = torch.randn(1, 8, 128, 128)


test_inputs = [query, key, value]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (512x64 and 1x1)

jit:
Failed running call_module L__self___q(*(FakeTensor(..., device='cuda:0', size=(1, 8, 64, 64)),), **{}):
a and b must have same reduction dim, but got [512, 64] X [1, 1].

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''