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
        self.conv2 = torch.nn.Conv2d(3, 3, 3)
        self.conv1_0 = torch.nn.Conv2d(3, 3, 3)
        self.conv1_1 = torch.nn.Conv3d(3, 3, 3)
        self.bn = torch.nn.BatchNorm2d(3)

    def forward(self, x1):
        s = self.conv1_0(x1)
        t = self.conv2(self.conv1_0(x1))
        y = self.conv1_1(s)
        y = self.bn(y)
        y = self.bn(y)
        return torch.abs(torch.sum(torch.norm(torch.cat((t, y), 1))))




func = Model().to('cuda')



x = torch.randn(1, 3, 6, 6)


test_inputs = [x]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [3, 3, 3, 3, 3], expected input[1, 1, 3, 4, 4] to have 3 channels, but got 1 channels instead

jit:
Failed running call_module L__self___conv1_1(*(FakeTensor(..., device='cuda:0', size=(1, 3, 4, 4)),), **{}):
Given groups=1, weight of size [3, 3, 3, 3, 3], expected input[1, 1, 3, 4, 4] to have 3 channels, but got 1 channels instead

from user code:
   File "<string>", line 27, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''