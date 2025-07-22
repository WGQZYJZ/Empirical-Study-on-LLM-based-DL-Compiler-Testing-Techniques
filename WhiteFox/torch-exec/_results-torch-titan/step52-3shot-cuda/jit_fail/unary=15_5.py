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
        self.conv1 = torch.nn.Conv2d(64, 96, kernel_size=5, stride=1, padding=2, bias=False)
        self.conv2 = torch.nn.Conv2d(192, 64, kernel_size=1, stride=1, padding=0, groups=1, bias=False)

    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = self.conv2(v1)
        v3 = torch.relu(v2)
        v4 = torch.relu(v3)
        return v4




func = Model().to('cuda')



x1 = torch.randn(2, 64, 96, 96)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [64, 192, 1, 1], expected input[2, 96, 96, 96] to have 192 channels, but got 96 channels instead

jit:
Failed running call_module L__self___conv2(*(FakeTensor(..., device='cuda:0', size=(2, 96, 96, 96)),), **{}):
Given groups=1, weight of size [64, 192, 1, 1], expected input[2, 96, 96, 96] to have 192 channels, but got 96 channels instead

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''