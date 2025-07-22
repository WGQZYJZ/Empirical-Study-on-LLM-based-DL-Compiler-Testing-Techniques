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
        self.conv1 = torch.nn.Conv2d(64, 256, 7, stride=1, padding=0)
        self.conv2 = torch.nn.Conv2d(1, 64, 7, stride=2, padding=3)

    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = (v1 - 1)
        v3 = F.relu(v2)
        v4 = v3.repeat(2, 1, 1, 1)
        v5 = self.conv2(v4)
        v6 = (v5 - 5)
        v7 = F.relu(v6)
        return v7




func = Model().to('cuda')



x1 = torch.randn(1, 64, 224, 224)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [64, 1, 7, 7], expected input[2, 256, 218, 218] to have 1 channels, but got 256 channels instead

jit:
Failed running call_module L__self___conv2(*(FakeTensor(..., device='cuda:0', size=(2, 256, 218, 218)),), **{}):
Given groups=1, weight of size [64, 1, 7, 7], expected input[2, 256, 218, 218] to have 1 channels, but got 256 channels instead

from user code:
   File "<string>", line 27, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''