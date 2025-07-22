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
        self.conv1 = torch.nn.Conv2d(32, 32, 2, stride=1, padding=0)
        self.conv2 = torch.nn.Conv2d(32, 128, 3, stride=1, padding=0)
        self.conv3 = torch.nn.Conv2d(1, 128, 9, stride=1, padding=0)

    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = self.conv2(v1)
        v3 = self.conv3(x1)
        v4 = (v2 + v3)
        v5 = (v4 * 0.5)
        v6 = (v4 * v4)
        v7 = (v6 * v4)
        v8 = (v7 * 0.044715)
        v9 = (v4 + v8)
        v10 = (v9 * 0.7978845608028654)
        v11 = torch.tanh(v10)
        v12 = (v11 + 1)
        v13 = (v5 * v12)
        return v13




func = Model().to('cuda')



x1 = torch.randn(1, 32, 32, 32)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [128, 1, 9, 9], expected input[1, 32, 32, 32] to have 1 channels, but got 32 channels instead

jit:
Failed running call_module L__self___conv3(*(FakeTensor(..., device='cuda:0', size=(1, 32, 32, 32)),), **{}):
Given groups=1, weight of size [128, 1, 9, 9], expected input[1, 32, 32, 32] to have 1 channels, but got 32 channels instead

from user code:
   File "<string>", line 26, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''