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



class Model2(torch.nn.Module):

    def __init__(self, _min, _max):
        super().__init__()
        self._min = 0
        self._max = 1
        self.linear = torch.nn.Linear(3, 4)

    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = torch.clamp_min(v1, self._min)
        v3 = torch.clamp_max(v2, self._max)
        return v3



_min = 1
_max = 1
func = Model2(float('-inf'), float('inf')).to('cuda')



x1 = torch.randn(1, 3, 64, 64)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (192x64 and 3x4)

jit:
Failed running call_module L__self___linear(*(FakeTensor(..., device='cuda:0', size=(1, 3, 64, 64)),), **{}):
a and b must have same reduction dim, but got [192, 64] X [3, 4].

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''