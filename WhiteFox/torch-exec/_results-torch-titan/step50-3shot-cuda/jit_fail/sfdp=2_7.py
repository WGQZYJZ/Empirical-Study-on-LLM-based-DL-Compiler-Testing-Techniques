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

    def __init__(self, num_heads=8, query_size=64):
        super().__init__()
        self.query = nn.Linear(query_size, query_size)
        self.key = nn.Linear(query_size, query_size)
        self.value = nn.Linear(query_size, query_size)
        self.inv_scale_factor = math.sqrt(query_size)
        self.dropout_p = 0.5
        self.num_heads = num_heads

    def forward(self, x1, x2, x3):
        v1 = self.query(x1)
        v2 = self.key(x2)
        v3 = self.value(x3)
        v4 = torch.matmul(v1, v2.transpose((- 2), (- 1)))
        v5 = v4.div(self.inv_scale_factor)
        v6 = v5.softmax(dim=(- 1))
        v7 = torch.nn.functional.dropout(v6, p=self.dropout_p)
        v8 = torch.matmul(v7, v3)
        return v8



func = Model().to('cuda')



x1 = torch.randn(1, 64, 14, 14)



x2 = torch.randn(1, 64, 14, 14)



x3 = torch.randn(1, 64, 14, 14)


test_inputs = [x1, x2, x3]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (896x14 and 64x64)

jit:
Failed running call_module L__self___query(*(FakeTensor(..., device='cuda:0', size=(1, 64, 14, 14)),), **{}):
a and b must have same reduction dim, but got [896, 14] X [64, 64].

from user code:
   File "<string>", line 27, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''