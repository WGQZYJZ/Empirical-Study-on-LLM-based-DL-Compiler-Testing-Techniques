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
        self.conv1 = torch.nn.Conv2d(32, 22, 7, stride=1, padding=3)
        self.conv2 = torch.nn.Conv2d(51, 6, 1, stride=1, padding=0)

    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = (v1 * 0.5)
        v3 = (v1 * 0.7071067811865476)
        v4 = torch.erf(v3)
        v5 = (v4 + 1)
        v6 = (v2 * v5)
        v7 = self.conv2(v6)
        return v7




func = Model().to('cuda')



x1 = torch.randn(1, 32, 28, 28)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [6, 51, 1, 1], expected input[1, 22, 28, 28] to have 51 channels, but got 22 channels instead

jit:
Failed running call_module L__self___conv2(*(FakeTensor(..., device='cuda:0', size=(1, 22, 28, 28)),), **{}):
Given groups=1, weight of size [6, 51, 1, 1], expected input[1, 22, 28, 28] to have 51 channels, but got 22 channels instead

from user code:
   File "<string>", line 29, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''