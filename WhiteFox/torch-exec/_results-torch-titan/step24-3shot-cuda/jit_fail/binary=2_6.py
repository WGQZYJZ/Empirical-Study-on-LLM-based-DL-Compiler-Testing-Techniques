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
        self.conv1 = torch.nn.Conv2d(3, 14, kernel_size=1, stride=2, padding=0, bias=False)
        self.conv2 = torch.nn.Conv2d(14, 100, kernel_size=2, stride=2, padding=1, bias=False)
        self.conv3 = torch.nn.Conv2d(100, 44, kernel_size=2, stride=1, padding=1)

    def forward(self, x):
        v1 = self.conv1(x)
        v2 = F.relu(v1)
        v3 = v2[:, :, :(- 1), :(- 1)]
        v4 = self.conv2(v2)
        v5 = F.relu(v4)
        v6 = self.conv3(v5)
        v7 = self.conv3(v2)
        v8 = (v6 - v7)
        return v8




func = Model().to('cuda')



x = torch.randn(1, 3, 32, 32)


test_inputs = [x]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [44, 100, 2, 2], expected input[1, 14, 16, 16] to have 100 channels, but got 14 channels instead

jit:
Failed running call_module L__self___conv3(*(FakeTensor(..., device='cuda:0', size=(1, 14, 16, 16)),), **{}):
Given groups=1, weight of size [44, 100, 2, 2], expected input[1, 14, 16, 16] to have 100 channels, but got 14 channels instead

from user code:
   File "<string>", line 30, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''