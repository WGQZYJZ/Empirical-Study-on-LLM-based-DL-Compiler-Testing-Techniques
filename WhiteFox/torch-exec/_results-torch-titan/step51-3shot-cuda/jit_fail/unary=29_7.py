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

    def __init__(self, min_value=(- 0.9), max_value=0.9):
        super().__init__()
        self.conv_transpose1d = torch.nn.ConvTranspose1d(2, 2, 3, stride=3)
        self.conv2d = torch.nn.Conv2d(2, 2, 3, stride=3)
        self.min_value = min_value
        self.max_value = max_value

    def forward(self, x3):
        v1 = self.conv_transpose1d(x3)
        v2 = torch.clamp_min(v1, self.min_value)
        v3 = torch.clamp_max(v2, self.max_value)
        v4 = self.conv2d(v3)
        return v4




func = Model().to('cuda')



x3 = torch.randn(1, 2, 40)


test_inputs = [x3]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [2, 2, 3, 3], expected input[1, 1, 2, 120] to have 2 channels, but got 1 channels instead

jit:
Failed running call_module L__self___conv2d(*(FakeTensor(..., device='cuda:0', size=(1, 2, 120)),), **{}):
Given groups=1, weight of size [2, 2, 3, 3], expected input[1, 1, 2, 120] to have 2 channels, but got 1 channels instead

from user code:
   File "<string>", line 28, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''