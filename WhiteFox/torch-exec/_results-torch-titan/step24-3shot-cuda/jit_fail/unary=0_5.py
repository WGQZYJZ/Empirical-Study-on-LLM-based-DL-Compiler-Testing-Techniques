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
        self.conv1 = torch.nn.Conv2d(54, 9, 7, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(41, 3, 1, stride=1, padding=1)

    def forward(self, x3):
        v1 = self.conv1(x3)
        v2 = (v1 * 0.5)
        v3 = (v1 * v1)
        v4 = (v3 * v1)
        v5 = (v4 * 0.044715)
        v6 = (v1 + v5)
        v7 = (v6 * 0.7978845608028654)
        v8 = torch.tanh(v7)
        v9 = (v8 + 1)
        v10 = (v2 * v9)
        v11 = self.conv2(v10)
        return v11




func = Model().to('cuda')



x3 = torch.randn(1, 54, 64, 64)


test_inputs = [x3]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [3, 41, 1, 1], expected input[1, 9, 60, 60] to have 41 channels, but got 9 channels instead

jit:
Failed running call_module L__self___conv2(*(FakeTensor(..., device='cuda:0', size=(1, 9, 60, 60)),), **{}):
Given groups=1, weight of size [3, 41, 1, 1], expected input[1, 9, 60, 60] to have 41 channels, but got 9 channels instead

from user code:
   File "<string>", line 33, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''