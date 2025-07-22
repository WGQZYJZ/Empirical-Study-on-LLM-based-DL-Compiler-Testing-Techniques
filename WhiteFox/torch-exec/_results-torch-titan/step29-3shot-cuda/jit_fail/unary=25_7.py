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

    def __init__(self, negative_slope):
        super().__init__()
        self.linear = torch.nn.Linear(1, 8)

    def forward(self, x1, _negative_slope):
        v1 = self.linear(x1)
        v2 = (v1 > 0)
        v3 = ((- _negative_slope) * v1)
        v4 = torch.where(v2, v1, v3)
        return v4




negative_slope = 0.1

func = Model(negative_slope).to('cuda')



x1 = torch.randn(2, 1, 8)

_negative_slope = 1

test_inputs = [x1, _negative_slope]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (2x8 and 1x8)

jit:
Failed running call_module L__self___linear(*(FakeTensor(..., device='cuda:0', size=(2, 1, 8)),), **{}):
a and b must have same reduction dim, but got [2, 8] X [1, 8].

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''