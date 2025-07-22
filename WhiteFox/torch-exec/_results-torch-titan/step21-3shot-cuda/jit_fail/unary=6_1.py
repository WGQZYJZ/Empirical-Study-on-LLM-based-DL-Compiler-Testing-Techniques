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
        self.conv = torch.nn.Conv2d(3, 16, 1, stride=1, padding=1)
        self.bn = torch.nn.BatchNorm2d(32)

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = (1 + v1)
        v3 = torch.clamp_min(v2, 0)
        v4 = torch.clamp_max(v3, 6)
        v5 = (v1 * v4)
        v6 = (v5 / 6)
        v7 = self.bn(v6)
        return v7




func = Model().to('cuda')



x1 = torch.randn(2, 3, 64, 64)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
running_mean should contain 16 elements not 32

jit:
Failed running call_module L__self___bn(*(FakeTensor(..., device='cuda:0', size=(2, 16, 66, 66)),), **{}):
running_mean should contain 16 elements not 32

from user code:
   File "<string>", line 29, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''