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



class TestModule(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.conv2d1 = torch.nn.Conv2d(3, 6, 3, padding=1, bias=False)
        self.conv_transpose2d1 = torch.nn.ConvTranspose2d(6, 3, 3, padding=1, output_padding=0, bias=False)
        self.bn = torch.nn.BatchNorm2d(3, eps=1.00000005e-05, momentum=0.0, affine=True, track_running_stats=True)
        self.relu6_module = torch.nn.Sequential(torch.nn.Conv2d(3, 10, kernel_size=(1, 1), stride=(1, 1), bias=False), torch.nn.BatchNorm2d(10, eps=1.00000005e-05, momentum=0.0, affine=True, track_running_stats=True), torch.nn.ReLU(inplace=False))

    def forward(self, x1):
        v1 = self.conv2d1(x1)
        v2 = self.bn(v1)
        v3 = torch.nn.functional.relu6(v2)
        v4 = self.conv_transpose2d1(v3)
        v5 = self.relu6_module(v4)
        return v5




func = TestModule().to('cuda')



x1 = torch.randn(1, 3, 64, 64)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
running_mean should contain 6 elements not 3

jit:
Failed running call_module L__self___bn(*(FakeTensor(..., device='cuda:0', size=(1, 6, 64, 64)),), **{}):
running_mean should contain 6 elements not 3

from user code:
   File "<string>", line 26, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''