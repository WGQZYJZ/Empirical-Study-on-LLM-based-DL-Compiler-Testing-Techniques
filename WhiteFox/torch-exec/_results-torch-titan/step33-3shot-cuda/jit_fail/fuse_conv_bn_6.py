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
        self.conv = torch.nn.Conv2d(5, 3, 3)
        self.bn = torch.nn.BatchNorm2d(3)
        self.pool = torch.nn.AvgPool2d(3)

    def forward(self, x4):
        y2 = self.conv(x4)
        y3 = self.pool(y2)
        y4 = self.bn(y3)
        y5 = torch.abs(self.conv(y4))
        return y5




func = Model().to('cuda')



x4 = torch.randn(1, 5, 3, 3)


test_inputs = [x4]

# JIT_FAIL
'''
direct:
Given input size: (3x1x1). Calculated output size: (3x0x0). Output size is too small

jit:
Failed running call_module L__self___pool(*(FakeTensor(..., device='cuda:0', size=(1, 3, 1, 1)),), **{}):
Given input size: (3x1x1). Calculated output size: (3x0x0). Output size is too small

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''