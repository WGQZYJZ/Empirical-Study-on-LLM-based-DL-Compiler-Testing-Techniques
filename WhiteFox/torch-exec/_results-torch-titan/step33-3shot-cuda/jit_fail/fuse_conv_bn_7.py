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
        self.conv1 = torch.nn.Conv2d(3, 64, 7)
        self.pad = torch.nn.ConstantPad2d((3, 3, 2, 2), 2.0)
        self.conv2 = torch.nn.Conv2d(64, 128, 6)
        self.bn = torch.nn.BatchNorm2d(3)

    def forward(self, x3):
        y = self.conv1(x3)
        z = self.pad(x3)
        w = self.conv2(z)
        v = self.pad(y)
        u = self.conv1(v)
        a = self.bn(u)
        b = torch.tanh(a)
        return (a, b, y, z, v, w)




func = Model().to('cuda')



x3 = torch.randn(1, 3, 10, 10)


test_inputs = [x3]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [128, 64, 6, 6], expected input[1, 3, 14, 16] to have 64 channels, but got 3 channels instead

jit:
Failed running call_module L__self___conv2(*(FakeTensor(..., device='cuda:0', size=(1, 3, 14, 16)),), **{}):
Given groups=1, weight of size [128, 64, 6, 6], expected input[1, 3, 14, 16] to have 64 channels, but got 3 channels instead

from user code:
   File "<string>", line 27, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''