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
        self.l1 = torch.nn.Linear(3072, 768, bias=True)

    def forward(self, x):
        v0 = torch.flatten(x, 1)
        v1 = self.l1(v0)
        v2 = torch.clamp_min(v1, min=(- 0.2514298553466797))
        v3 = torch.clamp_max(v2, max=0.5333021664619446)
        return v3



func = Model().to('cuda')



x_dummy = torch.randn(1, 3, 64, 64)


test_inputs = [x_dummy]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (1x12288 and 3072x768)

jit:
Failed running call_module L__self___l1(*(FakeTensor(..., device='cuda:0', size=(1, 12288)),), **{}):
a and b must have same reduction dim, but got [1, 12288] X [3072, 768].

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''