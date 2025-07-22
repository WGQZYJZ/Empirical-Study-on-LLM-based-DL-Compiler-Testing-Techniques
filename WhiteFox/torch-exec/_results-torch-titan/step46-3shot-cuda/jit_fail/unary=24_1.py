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
        self.conv1 = torch.nn.Conv2d(10, 20, 5, 2, 1)
        self.conv2d = torch.nn.Conv2d(100, 2, 1, 2, 1)

    def forward(self, x):
        negative_slope = 0.17976282
        v1 = self.conv1(x)
        v2 = (v1 > 0)
        v3 = (v1 * negative_slope)
        v4 = torch.where(v2, v1, v3)
        v5 = self.conv2d(v4)
        v6 = (v5 > 0)
        v7 = (v5 * negative_slope)
        v8 = torch.where(v6, v5, v7)
        return v8




func = Model().to('cuda')



x1 = torch.randn(1, 10, 200, 200)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [2, 100, 1, 1], expected input[1, 20, 99, 99] to have 100 channels, but got 20 channels instead

jit:
Failed running call_module L__self___conv2d(*(FakeTensor(..., device='cuda:0', size=(1, 20, 99, 99)),), **{}):
Given groups=1, weight of size [2, 100, 1, 1], expected input[1, 20, 99, 99] to have 100 channels, but got 20 channels instead

from user code:
   File "<string>", line 28, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''