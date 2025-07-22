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
        self.conv = torch.nn.Conv2d(3, 64, 3, stride=1, padding=1)
        self.conv1 = torch.nn.Conv2d(1, 60, 1, stride=1, padding=0)
        self.conv2 = torch.nn.Conv2d(60, 1, 3, stride=1, padding=0)
        self.tanh = torch.nn.Tanh()

    def forward(self, x1):
        t1 = self.conv(x1)
        y = torch.clamp(t1, 0, 6)
        t2 = self.conv1(y)
        t3 = self.conv2(t2)
        t4 = (3 + t3)
        t5 = torch.clamp(t4, 0, 6)
        t6 = (t3 * t5)
        t7 = (t6 / 6)
        t8 = self.tanh(t7)
        return t8




func = Model().to('cuda')



x1 = torch.randn(1, 3, 28, 28)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [60, 1, 1, 1], expected input[1, 64, 28, 28] to have 1 channels, but got 64 channels instead

jit:
Failed running call_module L__self___conv1(*(FakeTensor(..., device='cuda:0', size=(1, 64, 28, 28)),), **{}):
Given groups=1, weight of size [60, 1, 1, 1], expected input[1, 64, 28, 28] to have 1 channels, but got 64 channels instead

from user code:
   File "<string>", line 27, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''