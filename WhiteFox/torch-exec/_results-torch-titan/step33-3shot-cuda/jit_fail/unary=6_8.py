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
        self.conv = torch.nn.Conv2d(3, 3, 1, stride=1, padding=1)
        self.bn = torch.nn.BatchNorm2d(3)

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = (3 + v1)
        v3 = torch.clamp_min(v2, 0)
        v4 = torch.clamp_max(v3, 6)
        v5 = (v1 * v4)
        v6 = (v5 * 6)
        v7 = self.bn(v6)
        return v7




func = Model().to('cuda')



x1 = torch.randn(3, 2, 64, 64)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [3, 3, 1, 1], expected input[3, 2, 64, 64] to have 3 channels, but got 2 channels instead

jit:
Failed running call_module L__self___conv(*(FakeTensor(..., device='cuda:0', size=(3, 2, 64, 64)),), **{}):
Given groups=1, weight of size [3, 3, 1, 1], expected input[3, 2, 64, 64] to have 3 channels, but got 2 channels instead

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''