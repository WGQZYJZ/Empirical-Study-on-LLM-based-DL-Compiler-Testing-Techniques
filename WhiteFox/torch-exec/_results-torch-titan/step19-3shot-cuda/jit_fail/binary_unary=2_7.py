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
        self.conv1 = torch.nn.Conv2d(16, 32, 3, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(4, 32, 1, stride=1, padding=0)

    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = F.relu((v1 - 0.1))
        v3 = F.max_pool2d(v2, 2)
        v4 = (v3 - 0.5)
        v5 = F.relu(v4)
        v6 = self.conv2(v5)
        v7 = torch.tanh(v6)
        v8 = (v7 - 0.5)
        v9 = torch.sigmoid(v8)
        return v9




func = Model().to('cuda')



x1 = torch.randn(1, 16, 28, 28)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [32, 4, 1, 1], expected input[1, 32, 14, 14] to have 4 channels, but got 32 channels instead

jit:
Failed running call_module L__self___conv2(*(FakeTensor(..., device='cuda:0', size=(1, 32, 14, 14)),), **{}):
Given groups=1, weight of size [32, 4, 1, 1], expected input[1, 32, 14, 14] to have 4 channels, but got 32 channels instead

from user code:
   File "<string>", line 28, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''