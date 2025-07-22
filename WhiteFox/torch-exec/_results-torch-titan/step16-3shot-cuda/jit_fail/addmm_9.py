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
        self.m = torch.nn.Conv2d(3, 0, (444, 555), bias=True)

    def forward(self, x1, x2):
        v1 = self.m(x1)
        v2 = (v1 + x2)
        return v2




func = Model().to('cuda')



x1 = torch.randn(0, 1, 333, 555)



x2 = torch.randn(1, 0)


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
Given groups=1, expected weight to be at least 1 at dimension 0, but got weight of size [0, 3, 444, 555] instead

jit:
Failed running call_module L__self___m(*(FakeTensor(..., device='cuda:0', size=(0, 1, 333, 555)),), **{}):
Given groups=1, expected weight to be at least 1 at dimension 0, but got weight of size [0, 3, 444, 555] instead

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''