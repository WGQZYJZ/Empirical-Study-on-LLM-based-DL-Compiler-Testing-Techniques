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
        self.add1 = torch.nn.ReLU(inplace=False)
        self.conv1 = torch.nn.Conv2d(3, 512, 1, stride=1, padding=2, dilation=2)
        self.conv_bn_relu1 = torch.nn.Conv2d(512, 512, 1, stride=1, bias=True)
        self.conv_bn_relu2 = torch.nn.Conv2d(512, 512, 1, stride=1, bias=True)
        self.conv3 = torch.nn.Conv2d(512, 256, 1, stride=1, padding=0)
        self.conv4 = torch.nn.Conv2d(256, 512, 1, stride=1, padding=0)
        self.conv5 = torch.nn.Conv2d(256, 512, 3, stride=1, padding=1)
        self.conv6 = torch.nn.Conv2d(512, 256, 1, stride=1, padding=0)
        self.conv7 = torch.nn.Conv2d(256, 512, 3, stride=1, padding=3, dilation=3)
        self.conv8 = torch.nn.Conv2d(512, 512, 1, stride=1, padding=0, groups=512)

    def forward(self, x1):
        v1 = self.add1(x1)
        v2 = self.conv1(v1)
        v3 = self.conv_bn_relu1(v2)
        v3 = (v3 * 0.5)
        v4 = self.conv_bn_relu2(v3)
        v4 = (v4 * 0.7071067811865476)
        v5 = torch.erf(v4)
        v6 = (v5 + 1)
        v6 = (v2 * v6)
        v7 = self.conv3(v6)
        v8 = self.conv4(v7)
        v9 = self.conv5(v8)
        v10 = self.conv6(v9)
        v11 = self.add1(x1)
        v11 = self.conv7(v11)
        v12 = self.conv8(v11)
        return v12




func = Model().to('cuda')



x1 = torch.randn(1, 3, 64, 64)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [512, 256, 3, 3], expected input[1, 512, 68, 68] to have 256 channels, but got 512 channels instead

jit:
Failed running call_module L__self___conv5(*(FakeTensor(..., device='cuda:0', size=(1, 512, 68, 68)),), **{}):
Given groups=1, weight of size [512, 256, 3, 3], expected input[1, 512, 68, 68] to have 256 channels, but got 512 channels instead

from user code:
   File "<string>", line 42, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''