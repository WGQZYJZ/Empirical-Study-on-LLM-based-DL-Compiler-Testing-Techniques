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
        self.conv = torch.nn.Conv2d(1, 1, 1, stride=1, padding=0)
        self.conv1 = torch.nn.Conv2d(1, 8, 1, stride=1, padding=0)
        self.conv2 = torch.nn.Conv2d(8, 7, 7, stride=7, padding=0)

    def forward(self, x6):
        v1 = self.conv(x6)
        v2 = self.conv1(v1)
        v3 = self.conv2(v2)
        v4 = (v3 * 0.5)
        v5 = (v3 * v3)
        v6 = (v5 * v3)
        v7 = (v6 * 0.044715)
        v8 = (v3 + v7)
        v9 = (v8 * 0.7978845608028654)
        v10 = torch.tanh(v9)
        v11 = (v10 + 1)
        v12 = (v3 * v11)
        return v12




func = Model().to('cuda')



x6 = torch.randn(1, 1, 1, 1)


test_inputs = [x6]

# JIT_FAIL
'''
direct:
Calculated padded input size per channel: (1 x 1). Kernel size: (7 x 7). Kernel size can't be greater than actual input size

jit:
Failed running call_module L__self___conv2(*(FakeTensor(..., device='cuda:0', size=(1, 8, 1, 1)),), **{}):
Calculated padded input size per channel: (1 x 1). Kernel size: (7 x 7). Kernel size can't be greater than actual input size

from user code:
   File "<string>", line 26, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''