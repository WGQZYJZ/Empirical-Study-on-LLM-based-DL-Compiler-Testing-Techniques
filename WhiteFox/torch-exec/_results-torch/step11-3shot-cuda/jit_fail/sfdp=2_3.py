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

    def forward(self, query, key, value, scale_factor, dropout_p):
        _sum = query + key
        _sum2 = torch.nn.functional.relu(_sum)
        _sum3 = torch.nn.functional.softmax(_sum2, dim=-1)
        _sum4 = torch.nn.functional.dropout(_sum3, p=dropout_p)
        v1 = torch.matmul(_sum4, value)
        return v1


func = Model().to('cuda')


query = torch.randn(3, 8, 4)

key = torch.randn(3, 8, 8)

value = torch.randn(3, 8, 8)

scale_factor = torch.rand(1)
dropout_p = 1

test_inputs = [query, key, value, scale_factor, dropout_p]

# JIT_FAIL
'''
direct:
The size of tensor a (4) must match the size of tensor b (8) at non-singleton dimension 2

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., device='cuda:0', size=(s0, s1, s2)), FakeTensor(..., device='cuda:0', size=(s3, s4, s5))), **{}):
The size of tensor a (s2) must match the size of tensor b (s5) at non-singleton dimension 2)

from user code:
   File "<string>", line 19, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''