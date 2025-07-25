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
        self.conv1 = torch.nn.Conv2d(3, 10, 5, stride=2, padding=2)
        self.conv2 = torch.nn.Conv2d(5, 16, 5, stride=2, padding=2)
        self.conv3 = torch.nn.ConvTranspose2d(16, 5, 5, stride=2, padding=2)
        self.conv4 = torch.nn.ConvTranspose2d(10, 3, 5, stride=2, padding=2)

    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = (v1 - 0.5)
        v3 = F.relu(v2)
        v4 = self.conv2(v3)
        v5 = (v4 - 1.7)
        v6 = F.relu(v5)
        v7 = self.conv3(v6)
        v8 = (v7 - 2.2)
        v9 = F.relu(v8)
        v10 = torch.tanh(v9)
        v11 = self.conv4(v10)
        v12 = (v11 - 0.4)
        v13 = F.relu(v12)
        return v13




func = Model().to('cuda')



x1 = torch.randn(1, 3, 32, 32)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [16, 5, 5, 5], expected input[1, 10, 16, 16] to have 5 channels, but got 10 channels instead

jit:
Failed running call_module L__self___conv2(*(FakeTensor(..., device='cuda:0', size=(1, 10, 16, 16)),), **{}):
Given groups=1, weight of size [16, 5, 5, 5], expected input[1, 10, 16, 16] to have 5 channels, but got 10 channels instead

from user code:
   File "<string>", line 28, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''