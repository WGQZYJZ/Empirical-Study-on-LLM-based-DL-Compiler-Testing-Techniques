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

    def forward(self, x1, x2, x3):
        v1 = torch.matmul(x1, x2.transpose(-2, -1))
        v2 = v1.div(x3)
        v3 = v2.softmax(dim=-1)
        v4 = torch.nn.functional.dropout(v3, p=0.5)
        v5 = v4.matmul(x1)
        v6 = v5 + x2
        return v6


func = Model().to('cpu')


input_query = torch.randn(96, 8, 512)

input_key = torch.randn(96, 8, 512)

input_value = torch.randn(96, 8, 512)

test_inputs = [input_query, input_key, input_value]

# JIT_FAIL
'''
direct:
The size of tensor a (8) must match the size of tensor b (512) at non-singleton dimension 2

jit:
Failed running call_method div(*(FakeTensor(..., size=(s0, s4, s1)), FakeTensor(..., size=(s6, s7, s8))), **{}):
The size of tensor a (s1) must match the size of tensor b (s8) at non-singleton dimension 2)

from user code:
   File "<string>", line 20, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''