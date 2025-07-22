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
        self.m = torch.nn.Linear(8, 4)
        self.c = torch.nn.Linear(8, 4)

    def forward(self, x1):
        r1 = self.m(x1)
        r2 = self.c(x1)
        return ((r1 * (r2 + 3).clamp(min=0, max=6)) / 6)



func = Model().to('cuda')



x4 = torch.randn(1, 8, 32, 32)


test_inputs = [x4]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (256x32 and 8x4)

jit:
Failed running call_module L__self___m(*(FakeTensor(..., device='cuda:0', size=(1, 8, 32, 32)),), **{}):
a and b must have same reduction dim, but got [256, 32] X [8, 4].

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''