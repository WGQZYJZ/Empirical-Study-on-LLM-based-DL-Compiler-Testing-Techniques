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
        self.conv1 = torch.nn.Conv2d(3, 192, 8, stride=4, padding=2)
        self.conv2 = torch.nn.Conv2d(32, 768, 3, stride=1, padding=1)
        self.conv3 = torch.nn.Conv2d(768, 896, 2, stride=2, padding=1)
        self.conv4 = torch.nn.Conv2d(896, 376, 1, stride=1, padding=0)
        self.conv5 = torch.nn.Conv2d(376, 192, 1, stride=1, padding=0)

    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = torch.relu(v1)
        v3 = self.conv2(v2)
        v4 = torch.relu(v3)
        v5 = self.conv3(v4)
        v6 = torch.relu(v5)
        v7 = self.conv4(v6)
        v8 = torch.relu(v7)
        v9 = self.conv5(v8)
        v10 = torch.relu(v9)
        return v10




func = Model().to('cuda')



x1 = torch.randn(1, 3, 112, 112)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [768, 32, 3, 3], expected input[1, 192, 28, 28] to have 32 channels, but got 192 channels instead

jit:
Failed running call_module L__self___conv2(*(FakeTensor(..., device='cuda:0', size=(1, 192, 28, 28)),), **{}):
Given groups=1, weight of size [768, 32, 3, 3], expected input[1, 192, 28, 28] to have 32 channels, but got 192 channels instead

from user code:
   File "<string>", line 28, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''