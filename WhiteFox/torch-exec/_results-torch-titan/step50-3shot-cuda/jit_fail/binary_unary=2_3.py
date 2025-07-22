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
        self.conv1 = torch.nn.Conv2d(3, 8, 4, stride=8, padding=2)
        self.conv2 = torch.nn.Conv2d(16, 8, 3, stride=1, padding=1)

    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = (v1 - 0.2)
        v3 = F.relu(v2)
        v4 = self.conv2(v3)
        v5 = (v4 - 0.8)
        v6 = F.relu(v5)
        v7 = F.relu((v6 - 0.9))
        v8 = torch.squeeze(v7, 0)
        return v8




func = Model().to('cuda')



x1 = torch.randn(1, 3, 128, 128)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [8, 16, 3, 3], expected input[1, 8, 17, 17] to have 16 channels, but got 8 channels instead

jit:
Failed running call_module L__self___conv2(*(FakeTensor(..., device='cuda:0', size=(1, 8, 17, 17)),), **{}):
Given groups=1, weight of size [8, 16, 3, 3], expected input[1, 8, 17, 17] to have 16 channels, but got 8 channels instead

from user code:
   File "<string>", line 26, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''