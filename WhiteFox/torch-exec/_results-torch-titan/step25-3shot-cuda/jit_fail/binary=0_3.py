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
        self.conv1 = torch.nn.Conv2d(128, 1, 1, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(128, 3, 2, stride=1, padding=1)

    def forward(self, x1, other=1, padding1=None, bias1=None):
        v1 = self.conv1(x1)
        if ((other == 1) and (padding1 == None) and (bias1 == None)):
            other = torch.randn(v1.shape)
        v2 = self.conv2(v1)
        if ((padding1 == None) and (bias1 == None)):
            padding1 = torch.randn(v2.shape)
        v3 = (v2 + other)
        if (bias1 == None):
            bias1 = torch.randn(v3.shape)
        v4 = (v3 + padding1)
        return v4




func = Model().to('cuda')



x1 = torch.randn(1, 128, 256, 256)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [3, 128, 2, 2], expected input[1, 1, 258, 258] to have 128 channels, but got 1 channels instead

jit:
Failed running call_module L__self___conv2(*(FakeTensor(..., device='cuda:0', size=(1, 1, 258, 258)),), **{}):
Given groups=1, weight of size [3, 128, 2, 2], expected input[1, 1, 258, 258] to have 128 channels, but got 1 channels instead

from user code:
   File "<string>", line 26, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''