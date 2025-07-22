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
        self.conv2d_1 = torch.nn.Conv2d(3, 64, 3, bias=False)
        self.batchnorm1d_1 = torch.nn.BatchNorm2d(64)
        self.conv2d_2 = torch.nn.Conv2d(64, 64, 3)
        self.batchnorm1d_2 = torch.nn.BatchNorm1d(64)
        self.conv2d_3 = torch.nn.Conv2d(64, 32, 2)
        self.batchnorm1d_3 = torch.nn.BatchNorm1d(32)
        self.conv2d_4 = torch.nn.Conv2d(288, 64, 3, padding=1)
        self.batchnorm1d_4 = torch.nn.BatchNorm1d(64)
        self.avgpool = torch.nn.AdaptiveAvgPool2d((1, 1))

    def forward(self, x):
        x = self.conv2d_1(x)
        x = self.batchnorm1d_1(x)
        x = self.conv2d_2(x)
        x = self.batchnorm1d_2(x)
        x = torch.add(x, 0.1)
        x = self.conv2d_3(x)
        x = self.batchnorm1d_3(x)
        x = self.conv2d_4(x)
        x = self.batchnorm1d_4(x)
        x = self.avgpool(x)
        x = torch.flatten(x, 1)
        return x




func = Model().to('cuda')



x = torch.randn(1, 3, 224, 224)


test_inputs = [x]

# JIT_FAIL
'''
direct:
expected 2D or 3D input (got 4D input)

jit:
Failed running call_module L__self___batchnorm1d_2(*(FakeTensor(..., device='cuda:0', size=(1, 64, 220, 220)),), **{}):
expected 2D or 3D input (got 4D input)

from user code:
   File "<string>", line 33, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''