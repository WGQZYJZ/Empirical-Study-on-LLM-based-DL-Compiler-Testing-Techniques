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
        self.conv = torch.nn.Conv2d(32, 32, 3, stride=2, padding=1)
        self.conv2 = torch.nn.Conv2d(16, 16, 11, stride=4, padding=2)
        self.conv3 = torch.nn.Conv2d(2, 2, 1, stride=1, padding=0)

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = (v1 * 0.5)
        v3 = (v1 * 0.7071067811865476)
        v4 = torch.erf(v3)
        v5 = (v4 + 1)
        v6 = (v2 * v5)
        v7 = torch.tanh(v6)
        v8 = self.conv2(v7)
        v9 = self.conv3(v8)
        return v9




func = Model().to('cuda')



x1 = torch.randn(1, 32, 84, 72)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [16, 16, 11, 11], expected input[1, 32, 42, 36] to have 16 channels, but got 32 channels instead

jit:
Failed running call_module L__self___conv2(*(FakeTensor(..., device='cuda:0', size=(1, 32, 42, 36)),), **{}):
Given groups=1, weight of size [16, 16, 11, 11], expected input[1, 32, 42, 36] to have 16 channels, but got 32 channels instead

from user code:
   File "<string>", line 31, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''