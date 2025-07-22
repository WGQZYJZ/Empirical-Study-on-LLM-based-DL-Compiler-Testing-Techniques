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
        self.conv1 = torch.nn.Conv2d(64, 32, 5, stride=2, padding=2)
        self.conv2 = torch.nn.Conv2d(32, 1, 1, stride=2, padding=2)

    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = (v1 - 0.5)
        v3 = F.relu(v2)
        v4 = self.conv1(v3)
        v5 = (v4 - 1.5)
        v6 = F.relu(v5)
        v7 = torch.squeeze(v6, 0)
        return v7




func = Model().to('cuda')



x1 = torch.randn(1, 64, 64, 64)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [32, 64, 5, 5], expected input[1, 32, 32, 32] to have 64 channels, but got 32 channels instead

jit:
Failed running call_module L__self___conv1(*(FakeTensor(..., device='cuda:0', size=(1, 32, 32, 32)),), **{}):
Given groups=1, weight of size [32, 64, 5, 5], expected input[1, 32, 32, 32] to have 64 channels, but got 32 channels instead

from user code:
   File "<string>", line 26, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''