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
        self.conv = torch.nn.Conv2d(8, 10, 7, stride=1, padding=0)
        self.conv2 = torch.nn.Conv2d(10, 9, 15, stride=5, padding=1)
        self.conv3 = torch.nn.Conv2d(9, 8, 7, stride=1, padding=0)

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = (v1 * 0.5)
        v3 = (v1 * 0.7071067811865476)
        v4 = torch.erf(v3)
        v5 = (v4 + 1)
        v6 = (v2 * v5)
        v7 = self.conv2(v6)
        v8 = self.conv3(v7)
        return v8




func = Model().to('cuda')



x1 = torch.randn(1, 8, 81, 37)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Calculated padded input size per channel: (13 x 4). Kernel size: (7 x 7). Kernel size can't be greater than actual input size

jit:
Failed running call_module L__self___conv3(*(FakeTensor(..., device='cuda:0', size=(1, 9, 13, 4)),), **{}):
Calculated padded input size per channel: (13 x 4). Kernel size: (7 x 7). Kernel size can't be greater than actual input size

from user code:
   File "<string>", line 31, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''