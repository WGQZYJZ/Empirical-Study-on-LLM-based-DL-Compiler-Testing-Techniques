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



class ModelTanh(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 16, 3, padding=1)
        self.conv1x1 = torch.nn.Conv2d(16, 8, 1)
        self.conv3x3 = torch.nn.Conv2d(8, 8, 3, dilation=2, padding=3)
        self.conv = torch.nn.ReLU()

    def forward(self, x):
        v1 = self.conv(self.conv(self.conv(x)))
        v2 = self.conv1x1(v1)
        v3 = torch.tanh(self.conv(self.conv3x3(v2)))
        return v3




func = ModelTanh().to('cuda')



x = torch.randn(1, 3, 64, 64)


test_inputs = [x]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [8, 16, 1, 1], expected input[1, 3, 64, 64] to have 16 channels, but got 3 channels instead

jit:
Failed running call_module L__self___conv1x1(*(FakeTensor(..., device='cuda:0', size=(1, 3, 64, 64)),), **{}):
Given groups=1, weight of size [8, 16, 1, 1], expected input[1, 3, 64, 64] to have 16 channels, but got 3 channels instead

from user code:
   File "<string>", line 26, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''