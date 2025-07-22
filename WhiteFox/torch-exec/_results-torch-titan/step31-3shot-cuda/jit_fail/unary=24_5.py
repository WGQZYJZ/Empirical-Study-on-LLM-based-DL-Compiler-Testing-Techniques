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

    def __init__(self, nchan):
        super().__init__()
        self.conv_1 = torch.nn.Conv2d(nchan, nchan, 1, stride=1, padding=1)
        self.conv_2 = torch.nn.Conv2d(nchan, nchan, 1, stride=1, padding=1)

    def forward(self, x):
        negative_slope = 0.2
        v1 = self.conv_1(x)
        v2 = (v1 > 0)
        v3 = (v1 * negative_slope)
        v4 = torch.where(v2, v1, v3)
        v5 = self.conv_2(v4)
        return v5



nchan = 1

func = Model(nchan).to('cuda')



x1 = torch.randn(1, 8, 64, 64)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [1, 1, 1, 1], expected input[1, 8, 64, 64] to have 1 channels, but got 8 channels instead

jit:
Failed running call_module L__self___conv_1(*(FakeTensor(..., device='cuda:0', size=(1, 8, 64, 64)),), **{}):
Given groups=1, weight of size [1, 1, 1, 1], expected input[1, 8, 64, 64] to have 1 channels, but got 8 channels instead

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''