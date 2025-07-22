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
        self.conv1 = torch.nn.Conv2d(3, 1, 3, stride=1, padding=0)
        self.conv2 = torch.nn.Conv2d(4, 4, 9, stride=3, padding=0)
        self.conv3 = torch.nn.Conv2d(4, 2, 3, stride=1, padding=1)

    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = (v1 * 0.5)
        v3 = (v1 * 0.7071067811865476)
        v4 = torch.erf(v3)
        v5 = (v4 + 1)
        v6 = (v2 * v5)
        v6 = self.conv2(v6)
        v7 = (v6 * 0.5)
        v8 = (v6 * 0.7071067811865476)
        v9 = torch.erf(v8)
        v10 = (v9 + 1)
        v11 = (v7 * v10)
        v12 = (v11 + 1)
        v13 = self.conv3(v12)
        return v13




func = Model().to('cuda')



x1 = torch.randn(1, 3, 32, 32)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [4, 4, 9, 9], expected input[1, 1, 30, 30] to have 4 channels, but got 1 channels instead

jit:
Failed running call_module L__self___conv2(*(FakeTensor(..., device='cuda:0', size=(1, 1, 30, 30)),), **{}):
Given groups=1, weight of size [4, 4, 9, 9], expected input[1, 1, 30, 30] to have 4 channels, but got 1 channels instead

from user code:
   File "<string>", line 30, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''