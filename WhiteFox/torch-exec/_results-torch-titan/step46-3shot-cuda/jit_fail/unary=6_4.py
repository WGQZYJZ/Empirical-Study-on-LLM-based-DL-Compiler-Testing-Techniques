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
        self.conv1 = torch.nn.Conv2d(3, 12, 1, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(12, 18, 1, stride=1, padding=1)
        self.bn1 = torch.nn.BatchNorm2d(12)
        self.bn2 = torch.nn.BatchNorm2d(18)

    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = self.conv2(v1)
        v3 = self.bn1(v2)
        v4 = (v3 - 3)
        v5 = torch.clamp_max(v4, 6)
        v6 = (v3 * v5)
        v7 = self.bn2(v6)
        v8 = (v7 / 3)
        return v8




func = Model().to('cuda')



x1 = torch.randn(1, 3, 64, 64)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
running_mean should contain 18 elements not 12

jit:
Failed running call_module L__self___bn1(*(FakeTensor(..., device='cuda:0', size=(1, 18, 68, 68)),), **{}):
running_mean should contain 18 elements not 12

from user code:
   File "<string>", line 27, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''