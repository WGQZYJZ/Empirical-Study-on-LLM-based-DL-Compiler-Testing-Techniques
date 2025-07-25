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
        self.conv = torch.nn.Conv2d(3, 8, 3, stride=1, padding=1)

    def forward(self, x):
        v1 = self.conv(x)
        v2 = (v1 * 0.5)
        v3 = (v1 * 0.7071067811865476)
        v4 = torch.erf(v3)
        v5 = (v4 + 1)
        v6 = (v2 * v5)
        v7 = torch.cat([torch.cat([v6, v1], dim=1) for i in range(4)])
        v8 = torch.cat([torch.cat([v7, v1], dim=0) for i in range(3)])
        v9 = torch.cat([torch.cat([v8, v1], dim=2) for i in range(3)])
        v10 = torch.cat([torch.cat([v9, v1], dim=3) for i in range(3)])
        return v10



func = Model().to('cuda')



x = torch.randn(2, 6, 64, 64)


test_inputs = [x]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [8, 3, 3, 3], expected input[2, 6, 64, 64] to have 3 channels, but got 6 channels instead

jit:
Failed running call_module L__self___conv(*(FakeTensor(..., device='cuda:0', size=(2, 6, 64, 64)),), **{}):
Given groups=1, weight of size [8, 3, 3, 3], expected input[2, 6, 64, 64] to have 3 channels, but got 6 channels instead

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''