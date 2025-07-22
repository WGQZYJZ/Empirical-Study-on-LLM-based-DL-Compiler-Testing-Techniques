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

    def __init__(self, min_value=0, max_value=0):
        super().__init__()
        self.conv = torch.nn.Conv2d(256, 32, 1, stride=1, padding=0)
        self.conv_transpose = torch.nn.ConvTranspose2d(32, 16, 75, stride=53, padding=0)
        self.min_value = min_value
        self.max_value = max_value

    def forward(self, x1):
        v1 = self.conv_transpose(x1)
        v2 = torch.clamp_min(v1, self.min_value)
        v3 = torch.clamp_max(v2, self.max_value)
        v4 = v3
        return v4




func = Model().to('cuda')



x1 = torch.randn(1, 256, 1, 1)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given transposed=1, weight of size [32, 16, 75, 75], expected input[1, 256, 1, 1] to have 32 channels, but got 256 channels instead

jit:
Failed running call_module L__self___conv_transpose(*(FakeTensor(..., device='cuda:0', size=(1, 256, 1, 1)),), **{}):
Given transposed=1, weight of size [32, 16, 75, 75], expected input[1, 256, 1, 1] to have 32 channels, but got 256 channels instead

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''