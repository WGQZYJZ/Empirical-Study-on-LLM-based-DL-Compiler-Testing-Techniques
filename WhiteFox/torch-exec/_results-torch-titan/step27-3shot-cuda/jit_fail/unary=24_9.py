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
        self.conv1 = torch.nn.Conv2d(128, 64, 1, stride=1, padding=0)
        self.conv2 = torch.nn.Conv2d(64, 1, 7, stride=1, padding=0)

    def forward(self, x):
        v1 = self.conv1(x)
        v2 = self.conv1(v1)
        v3 = self.conv2(v2)
        v4 = (v3 > 0.5)
        v5 = torch.where(v4, torch.tensor(1.0), torch.tensor(0.0))
        return v5




func = Model().to('cuda')



x1 = torch.rand(1, 128, 224, 224)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [64, 128, 1, 1], expected input[1, 64, 224, 224] to have 128 channels, but got 64 channels instead

jit:
Failed running call_module L__self___conv1(*(FakeTensor(..., device='cuda:0', size=(1, 64, 224, 224)),), **{}):
Given groups=1, weight of size [64, 128, 1, 1], expected input[1, 64, 224, 224] to have 128 channels, but got 64 channels instead

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''