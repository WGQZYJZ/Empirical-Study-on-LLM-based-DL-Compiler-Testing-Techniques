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
        self.conv1 = torch.nn.Conv2d(1, 3, 32, stride=4, padding=4)
        self.conv2 = torch.nn.Conv2d(3, 3, 32, stride=2, padding=1)

    def forward(self, x4):
        v1 = self.conv1(x4)
        v2 = self.conv2(v1)
        v3 = (v2 * 0.5)
        v4 = (v2 * v2)
        v5 = (v4 * v2)
        v6 = (v5 * 0.044715)
        v7 = (v2 + v6)
        v8 = (v7 * 0.7978845608028654)
        v9 = torch.tanh(v8)
        v10 = (v9 + 1)
        v11 = (v3 * v10)
        return v11




func = Model().to('cuda')



x4 = torch.randn(1, 1, 64, 64)


test_inputs = [x4]

# JIT_FAIL
'''
direct:
Calculated padded input size per channel: (13 x 13). Kernel size: (32 x 32). Kernel size can't be greater than actual input size

jit:
Failed running call_module L__self___conv2(*(FakeTensor(..., device='cuda:0', size=(1, 3, 11, 11)),), **{}):
Calculated padded input size per channel: (13 x 13). Kernel size: (32 x 32). Kernel size can't be greater than actual input size

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''