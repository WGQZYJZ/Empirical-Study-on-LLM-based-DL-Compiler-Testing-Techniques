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
        self.conv1 = torch.nn.Conv2d(1, 3, 3, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(1, 3, 3, stride=1, padding=1)
        self.conv3 = torch.nn.Conv2d(1, 5, 3, stride=1, padding=1)

    def forward(self, x1, x2, x3, x4):
        v1 = self.conv1(x1)
        v2 = (v1 + x2)
        v3 = torch.relu(v2)
        v4 = self.conv2(x3)
        v5 = (v4 + x4)
        v6 = torch.relu(v5)
        v7 = self.conv3(v3)
        v8 = (v7 + v6)
        v9 = torch.relu(v8)
        return v9




func = Model().to('cuda')



x1 = torch.randn(1, 1, 64, 64)



x2 = torch.randn(1, 1, 64, 64)



x3 = torch.randn(1, 1, 64, 64)



x4 = torch.randn(1, 1, 64, 64)


test_inputs = [x1, x2, x3, x4]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [5, 1, 3, 3], expected input[1, 3, 64, 64] to have 1 channels, but got 3 channels instead

jit:
Failed running call_module L__self___conv3(*(FakeTensor(..., device='cuda:0', size=(1, 3, 64, 64)),), **{}):
Given groups=1, weight of size [5, 1, 3, 3], expected input[1, 3, 64, 64] to have 1 channels, but got 3 channels instead

from user code:
   File "<string>", line 30, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''