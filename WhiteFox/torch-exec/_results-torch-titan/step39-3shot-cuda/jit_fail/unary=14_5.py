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
        self.conv2d_0 = torch.nn.Conv2d(221, 32, 3, stride=2, padding=1, dilation=1)
        self.conv_transpose_1 = torch.nn.ConvTranspose3d(32, 121, 3, stride=1, padding=1)

    def forward(self, x1):
        v1 = self.conv2d_0(x1)
        t1 = v1
        v2 = self.conv_transpose_1(t1)
        v3 = torch.sigmoid(v2)
        v4 = (v2 * v3)
        v5 = torch.sigmoid(v3)
        v7 = (v5 * v4)
        v8 = torch.clamp(v7, 0.0, 6.0)
        return v8




func = Model().to('cuda')



x1 = torch.randn(1, 221, 147, 147)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given transposed=1, weight of size [32, 121, 3, 3, 3], expected input[1, 1, 32, 74, 74] to have 32 channels, but got 1 channels instead

jit:
Failed running call_module L__self___conv_transpose_1(*(FakeTensor(..., device='cuda:0', size=(1, 32, 74, 74)),), **{}):
Given transposed=1, weight of size [32, 121, 3, 3, 3], expected input[1, 1, 32, 74, 74] to have 32 channels, but got 1 channels instead

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''