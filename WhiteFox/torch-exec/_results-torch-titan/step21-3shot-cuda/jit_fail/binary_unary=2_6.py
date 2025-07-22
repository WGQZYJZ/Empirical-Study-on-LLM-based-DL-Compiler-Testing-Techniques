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
        self.conv1 = torch.nn.Conv2d(64, 8, 4, stride=2, padding=1)
        self.conv2 = torch.nn.Conv2d(64, 8, 3, stride=2, padding=1)
        self.conv3 = torch.nn.Conv2d(8, 8, 3, stride=1, padding=0)

    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = F.gelu(v1)
        v3 = (v2 - 0.2)
        v4 = F.relu(v3)
        v5 = self.conv2(v4)
        v6 = F.gelu(v5)
        v7 = (v6 - 1)
        v8 = F.relu(v7)
        v9 = self.conv3(v8)
        v10 = (v9 - 0.5)
        v11 = F.relu(v10)
        return v11




func = Model().to('cuda')



x1 = torch.randn(1, 64, 64, 64)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [8, 64, 3, 3], expected input[1, 8, 32, 32] to have 64 channels, but got 8 channels instead

jit:
Failed running call_module L__self___conv2(*(FakeTensor(..., device='cuda:0', size=(1, 8, 32, 32)),), **{}):
Given groups=1, weight of size [8, 64, 3, 3], expected input[1, 8, 32, 32] to have 64 channels, but got 8 channels instead

from user code:
   File "<string>", line 28, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''