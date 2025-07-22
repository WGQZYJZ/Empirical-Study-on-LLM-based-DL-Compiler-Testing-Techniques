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
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=2, padding=1)
        self.conv2 = torch.nn.Conv2d(3, 8, 1, stride=2, padding=1)
        self.conv3 = torch.nn.Conv2d(3, 8, 1, stride=2, padding=1)
        self.conv4 = torch.nn.Conv2d(3, 8, 1, stride=2, padding=1)
        self.conv5 = torch.nn.Conv2d(3, 8, 1, stride=2, padding=1)

    def forward(self, x1, x2):
        m1 = (x1 + x2)
        m2 = (x1 * x2)
        m3 = (x1 - x2)
        m4 = (x1 / (0.1 + x2))
        m5 = (x1 + x2)
        v1 = torch.cat([m2, m3, m4], dim=1)
        v2 = self.conv1(v1)
        v3 = self.conv2(v2)
        v4 = self.conv3(v3)
        v5 = self.conv4(v3)
        v6 = self.conv5(v3)
        v7 = v5
        v7 = (v5 + m5)
        return v7




func = Model().to('cuda')



x1 = torch.randn(1, 3, 16, 16)



x2 = torch.randn(1, 3, 16, 16)


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [8, 3, 1, 1], expected input[1, 9, 16, 16] to have 3 channels, but got 9 channels instead

jit:
Failed running call_module L__self___conv1(*(FakeTensor(..., device='cuda:0', size=(1, 9, 16, 16)),), **{}):
Given groups=1, weight of size [8, 3, 1, 1], expected input[1, 9, 16, 16] to have 3 channels, but got 9 channels instead

from user code:
   File "<string>", line 32, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''