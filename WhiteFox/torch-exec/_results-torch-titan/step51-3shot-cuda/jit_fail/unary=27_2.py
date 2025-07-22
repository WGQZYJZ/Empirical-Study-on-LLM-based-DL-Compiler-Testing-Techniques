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

    def __init__(self, min, max):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 16, 51, stride=35, padding=8, dilation=48)
        self.min = min
        self.max = max

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.clamp_min(v1, self.min)
        v3 = torch.clamp_max(v2, self.max)
        return v3




min = (- 0.8636441)


max = 0.98630943


func = Model(min, max).to('cuda')



x1 = torch.randn(1, 3, 67, 167)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Calculated padded input size per channel: (83 x 183). Kernel size: (2401 x 2401). Kernel size can't be greater than actual input size

jit:
Failed running call_module L__self___conv(*(FakeTensor(..., device='cuda:0', size=(1, 3, 67, 167)),), **{}):
Calculated padded input size per channel: (83 x 183). Kernel size: (2401 x 2401). Kernel size can't be greater than actual input size

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''