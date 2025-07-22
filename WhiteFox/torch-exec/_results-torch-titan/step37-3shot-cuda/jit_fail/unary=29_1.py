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

    def __init__(self, min_value=1.9, max_value=(- 2.5)):
        super().__init__()
        self.conv_transpose2d = torch.nn.ConvTranspose2d(3, 8, 1, stride=1, padding=1)
        self.conv_transpose3d = torch.nn.ConvTranspose3d(8, 16, 2, stride=1, padding=1)
        self.min_value = min_value
        self.max_value = max_value

    def forward(self, x1):
        v1 = self.conv_transpose2d(x1)
        v2 = torch.clamp_min(v1, self.min_value)
        v3 = torch.clamp_max(v2, self.max_value)
        v4 = self.conv_transpose3d(v3)
        return v4




func = Model().to('cuda')



x1 = torch.randn(1, 3, 64, 64)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given transposed=1, weight of size [8, 16, 2, 2, 2], expected input[1, 1, 8, 62, 62] to have 8 channels, but got 1 channels instead

jit:
Failed running call_module L__self___conv_transpose3d(*(FakeTensor(..., device='cuda:0', size=(1, 8, 62, 62)),), **{}):
Given transposed=1, weight of size [8, 16, 2, 2, 2], expected input[1, 1, 8, 62, 62] to have 8 channels, but got 1 channels instead

from user code:
   File "<string>", line 28, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''