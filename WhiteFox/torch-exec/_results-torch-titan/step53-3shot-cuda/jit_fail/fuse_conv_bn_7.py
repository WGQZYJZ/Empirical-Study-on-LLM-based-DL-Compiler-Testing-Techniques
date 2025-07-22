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
        super(Model, self).__init__()
        self.conv1 = torch.nn.Conv2d(2, 3, 3, 1, 1, 1)
        self.bn1 = torch.nn.BatchNorm2d(2)
        self.conv2 = torch.nn.Conv2d(1, 16, 7)
        self.bn2 = torch.nn.BatchNorm2d(16)
        self.conv3 = torch.nn.Conv2d(1, 1, 1)
        self.bn3 = torch.nn.BatchNorm2d(1, affine=True)

    def forward(self, inputs):
        x1 = self.conv1(inputs)
        x2 = self.bn1(x1)
        x3 = self.conv2(x2)
        x4 = self.bn2(x3)
        x5 = self.conv3(x4)
        x6 = self.bn3(x5)
        return x6




class Model2(torch.nn.Module):

    def __init__(self):
        super(Model2, self).__init__()
        self.conv1 = torch.nn.Conv2d(2, 3, 3, 1, 1, 1, bias=False)
        self.bn1 = torch.nn.BatchNorm2d(2, affine=True)
        self.conv2 = torch.nn.Conv2d(1, 16, 7, bias=False)
        self.bn2 = torch.nn.BatchNorm2d(16, affine=True)
        self.conv3 = torch.nn.Conv2d(1, 1, 1, bias=False)
        self.bn3 = torch.nn.BatchNorm2d(1)

    def forward(self, inputs):
        x1 = self.conv1(inputs)
        x2 = self.bn1(x1)
        x3 = self.conv2(x2)
        x4 = self.bn2(x3)
        x5 = self.conv3(x4)
        x6 = self.bn3(x5)
        return x6




func = Model2().to('cuda')



inputs = torch.randn(1, 2, 224, 224)


test_inputs = [inputs]

# JIT_FAIL
'''
direct:
running_mean should contain 3 elements not 2

jit:
Failed running call_module L__self___bn1(*(FakeTensor(..., device='cuda:0', size=(1, 3, 224, 224)),), **{}):
running_mean should contain 3 elements not 2

from user code:
   File "<string>", line 51, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''