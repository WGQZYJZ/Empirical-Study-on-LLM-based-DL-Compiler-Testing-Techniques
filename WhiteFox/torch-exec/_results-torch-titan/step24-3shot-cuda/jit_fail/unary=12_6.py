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
        self.conv = torch.nn.Conv2d(72, 13, 63, stride=8, padding=16, dilation=9)

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1.tanh()
        v3 = v2.mul(v1)
        return v3




func = Model().to('cuda')



x1 = torch.randn(1, 72, 16, 16)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Calculated padded input size per channel: (48 x 48). Kernel size: (559 x 559). Kernel size can't be greater than actual input size

jit:
Failed running call_module L__self___conv(*(FakeTensor(..., device='cuda:0', size=(1, 72, 16, 16)),), **{}):
Calculated padded input size per channel: (48 x 48). Kernel size: (559 x 559). Kernel size can't be greater than actual input size

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''