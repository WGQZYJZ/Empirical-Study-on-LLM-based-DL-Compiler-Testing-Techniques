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
        self.conv1 = torch.nn.Conv2d(16, 16, 7, stride=1, padding=3)
        self.conv2 = torch.nn.Conv2d(16, 16, 7, stride=1, padding=3)

    def forward(self, x):
        v1 = self.conv1(x)
        v2 = (v1 + x)
        v3 = torch.relu(v2)
        v4 = self.conv2(v3)
        v5 = (1 + v4)
        v6 = torch.relu(v5)
        return torch.cat([v2, v5], dim=1)




func = Model().to('cuda')



x1 = torch.randn(10, 1, 3, 3)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [16, 16, 7, 7], expected input[10, 1, 3, 3] to have 16 channels, but got 1 channels instead

jit:
Failed running call_module L__self___conv1(*(FakeTensor(..., device='cuda:0', size=(10, 1, 3, 3)),), **{}):
Given groups=1, weight of size [16, 16, 7, 7], expected input[10, 1, 3, 3] to have 16 channels, but got 1 channels instead

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''