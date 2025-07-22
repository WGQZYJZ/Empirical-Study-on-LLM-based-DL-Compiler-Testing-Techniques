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
        self.conv1 = torch.nn.Conv2d(1, 2, 3, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(1, 2, 3, stride=1)
        self.conv3 = torch.nn.Conv2d(2, 4, 3, stride=1, padding=1)
        self.conv4 = torch.nn.Conv2d(2, 4, 3, stride=1, padding=1)
        self.conv5 = torch.nn.Conv2d(4, 8, 3, stride=1, padding=1)
        self.conv6 = torch.nn.Conv2d(4, 8, 3, stride=1, padding=1)

    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = torch.relu(v1)
        v3 = self.conv2(v1)
        v4 = self.conv3(v2)
        v5 = torch.relu(v4)
        v6 = self.conv4(v4)
        v7 = self.conv5(v5)
        v8 = torch.relu(v7)
        v9 = self.conv6(v7)
        return (v8 + v9)




func = Model().to('cuda')



x1 = torch.randn(1, 1, 64, 64)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [2, 1, 3, 3], expected input[1, 2, 64, 64] to have 1 channels, but got 2 channels instead

jit:
Failed running call_module L__self___conv2(*(FakeTensor(..., device='cuda:0', size=(1, 2, 64, 64)),), **{}):
Given groups=1, weight of size [2, 1, 3, 3], expected input[1, 2, 64, 64] to have 1 channels, but got 2 channels instead

from user code:
   File "<string>", line 29, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''