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
        self.conv = torch.nn.Conv2d(10, 11, 5, stride=3, padding=0)

    def forward(self, x):
        negative_slope = 1
        v1 = self.conv(x)
        v2 = (v1 > 0)
        v3 = (v1 * negative_slope)
        v4 = torch.where(v2, v1, v3)
        return v4




func = Model().to('cuda')



x1 = torch.randn(1, 11, 11, 11)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [11, 10, 5, 5], expected input[1, 11, 11, 11] to have 10 channels, but got 11 channels instead

jit:
Failed running call_module L__self___conv(*(FakeTensor(..., device='cuda:0', size=(1, 11, 11, 11)),), **{}):
Given groups=1, weight of size [11, 10, 5, 5], expected input[1, 11, 11, 11] to have 10 channels, but got 11 channels instead

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''