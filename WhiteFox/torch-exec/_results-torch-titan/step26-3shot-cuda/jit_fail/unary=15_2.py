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
        self.bn1 = torch.nn.BatchNorm2d(1)
        self.bn2 = torch.nn.BatchNorm2d(16)
        self.bn3 = torch.nn.BatchNorm2d(32)
        self.conv1 = torch.nn.Conv2d(1, 8, 1, stride=1, padding=0)
        self.conv2 = torch.nn.Conv2d(16, 16, 1, stride=1, padding=0)
        self.conv3 = torch.nn.Conv2d(32, 32, 1, stride=1, padding=0)

    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = torch.relu(self.bn1(v1))
        v3 = v2.reshape(4, 8, 8)
        v4 = v3.unsqueeze(2)
        v5 = self.conv2(v4)
        v6 = v5.reshape(4, 16, 4)
        v7 = v6.unsqueeze(2)
        v8 = self.conv3(v7)
        v9 = v8.reshape(4, 32, 2)
        v10 = v9.unsqueeze(2)
        return v10




func = Model().to('cuda')



x1 = torch.randn(64, 1, 4, 2)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
running_mean should contain 8 elements not 1

jit:
Failed running call_module L__self___bn1(*(FakeTensor(..., device='cuda:0', size=(64, 8, 4, 2)),), **{}):
running_mean should contain 8 elements not 1

from user code:
   File "<string>", line 28, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''