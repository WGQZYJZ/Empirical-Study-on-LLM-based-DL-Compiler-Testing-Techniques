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
        self.conv1 = torch.nn.Conv2d(16, 6, 3, stride=2, padding=2)
        self.conv2 = torch.nn.Conv2d(1, 16, 1, stride=1, padding=0)
        self.conv3 = torch.nn.Conv2d(6, 6, 1, stride=1, padding=0)
        self.conv4 = torch.nn.Conv2d(6, 6, 1, stride=1, padding=0)

    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = self.conv1(x1)
        v3 = self.conv2(x1)
        v4 = self.conv2(x1)
        v5 = self.conv3(torch.relu(v1))
        v6 = self.conv3(torch.relu(v2))
        v7 = self.conv4(((((torch.relu(v3) + torch.relu(v4)) + v5) + v6) + torch.relu(v1)))
        v8 = torch.relu(v7)
        return v8




func = Model().to('cuda')



x1 = torch.randn(1, 3, 64, 64)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [6, 16, 3, 3], expected input[1, 3, 64, 64] to have 16 channels, but got 3 channels instead

jit:
Failed running call_module L__self___conv1(*(FakeTensor(..., device='cuda:0', size=(1, 3, 64, 64)),), **{}):
Given groups=1, weight of size [6, 16, 3, 3], expected input[1, 3, 64, 64] to have 16 channels, but got 3 channels instead

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''