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
        self.conv = torch.nn.Conv2d(2, 42, 6, stride=2, padding=2)
        self.conv_a = torch.nn.Conv2d(17, 9, 3, stride=1, padding=1)
        self.conv_b = torch.nn.Conv2d(9, 19, 3, stride=1, padding=1)
        self.min = min
        self.max = max

    def forward(self, x1):
        v1 = self.conv(x1)
        v1 = ((v1 + self.conv_a(v1)) + self.conv_b(v1))
        v2 = torch.clamp_min(v1, self.min)
        v3 = torch.clamp_max(v2, self.max)
        return v3




min = (- 1.0)


max = 0.5


func = Model(min, max).to('cuda')



x1 = torch.randn(1, 2, 62, 62)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [9, 17, 3, 3], expected input[1, 42, 31, 31] to have 17 channels, but got 42 channels instead

jit:
Failed running call_module L__self___conv_a(*(FakeTensor(..., device='cuda:0', size=(1, 42, 31, 31)),), **{}):
Given groups=1, weight of size [9, 17, 3, 3], expected input[1, 42, 31, 31] to have 17 channels, but got 42 channels instead

from user code:
   File "<string>", line 27, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''