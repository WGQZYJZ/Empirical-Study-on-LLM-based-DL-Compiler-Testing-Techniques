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
        self.conv = torch.nn.Conv2d(64, 8, 1, stride=1, padding=0)
        self.conv1 = torch.nn.ConvTranspose2d(8, 8, 1, stride=3, padding=1)
        self.conv2 = torch.nn.Conv2d(8, 64, 3, stride=2, padding=1)
        self.conv4 = torch.nn.Conv2d(8, 64, 3, stride=2, padding=1)

    def forward(self, x13):
        v1 = self.conv(x13)
        v2 = self.conv1(v1)
        v3 = self.conv2(v2)
        v4 = self.conv4(v1)
        v5 = (v4 * 0.5)
        v6 = (v4 * v4)
        v7 = (v6 * v4)
        v8 = (v7 * 0.044715)
        v9 = (v4 + v8)
        v10 = (v9 * 0.7978845608028654)
        v11 = torch.tanh(v10)
        v12 = (v11 + 1)
        v13 = (v5 * v12)
        return v13




func = Model().to('cuda')



x13 = torch.randn(1, 8, 32, 32)


test_inputs = [x13]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [8, 64, 1, 1], expected input[1, 8, 32, 32] to have 64 channels, but got 8 channels instead

jit:
Failed running call_module L__self___conv(*(FakeTensor(..., device='cuda:0', size=(1, 8, 32, 32)),), **{}):
Given groups=1, weight of size [8, 64, 1, 1], expected input[1, 8, 32, 32] to have 64 channels, but got 8 channels instead

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''