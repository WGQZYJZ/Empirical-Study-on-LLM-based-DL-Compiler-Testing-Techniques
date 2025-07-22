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
        self.linear = torch.nn.Linear(16, 16)

    def forward(self, x1, min_value, max_value):
        v1 = self.linear(x1)
        v2 = torch.clamp_min(v1, min_value)
        v3 = torch.clamp_max(v2, max_value)
        return v3



func = Model().to('cuda')



x1 = torch.randn(1, 32, 64, 64)

min_value = 1
max_value = 1

test_inputs = [x1, min_value, max_value]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (2048x64 and 16x16)

jit:
Failed running call_module L__self___linear(*(FakeTensor(..., device='cuda:0', size=(1, 32, 64, 64)),), **{}):
a and b must have same reduction dim, but got [2048, 64] X [16, 16].

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''