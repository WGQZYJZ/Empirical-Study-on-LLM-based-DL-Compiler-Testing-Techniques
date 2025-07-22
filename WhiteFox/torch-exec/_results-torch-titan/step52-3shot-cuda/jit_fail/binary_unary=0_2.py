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
        self.dense1 = torch.nn.Linear(16, 16)
        self.conv1 = torch.nn.Conv2d(16, 16, 7, stride=1, padding=3)
        self.conv2 = torch.nn.Conv2d(16, 16, 7, stride=1, padding=3)

    def forward(self, x1, x2, x3):
        v1 = self.dense1(x1)
        v2 = (v1[:, None, None] + x1)
        v3 = self.conv1(v2)
        v4 = (v3 + v2)
        v5 = (v4 + x2)
        v6 = torch.nn.ReLU()(v5)
        v7 = self.conv2(v6)
        v8 = (v7 + x3)
        v9 = torch.relu(v8)
        return v9




func = Model().to('cuda')



x1 = torch.randn(1, 16)



x2 = torch.randn(1, 16, 64, 64)



x3 = torch.randn(1, 16, 64, 64)


test_inputs = [x1, x2, x3]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [16, 16, 7, 7], expected input[1, 1, 1, 16] to have 16 channels, but got 1 channels instead

jit:
Failed running call_module L__self___conv1(*(FakeTensor(..., device='cuda:0', size=(1, 1, 1, 16)),), **{}):
Given groups=1, weight of size [16, 16, 7, 7], expected input[1, 1, 1, 16] to have 16 channels, but got 1 channels instead

from user code:
   File "<string>", line 26, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''