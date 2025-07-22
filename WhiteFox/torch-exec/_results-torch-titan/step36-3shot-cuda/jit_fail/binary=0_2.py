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
        self.conv = torch.nn.Conv2d(64, 64, 1, stride=1, padding=1)

    def forward(self, x1, other=1, padding1=None, padding2=None, padding3=None, padding4=None):
        v1 = self.conv(x1)
        if (padding1 == None):
            padding1 = torch.randn(v1.shape)
        v2 = (v1 + other)
        v3 = torch.cat([v2, padding1])
        v4 = torch.cat([v3, padding2])
        v5 = torch.cat([v4, padding3])
        v6 = torch.cat([v5, padding4])
        return v6




func = Model().to('cuda')



x1 = torch.randn(3, 64, 64)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [64, 64, 1, 1], expected input[1, 3, 64, 64] to have 64 channels, but got 3 channels instead

jit:
Failed running call_module L__self___conv(*(FakeTensor(..., device='cuda:0', size=(3, 64, 64)),), **{}):
Given groups=1, weight of size [64, 64, 1, 1], expected input[1, 3, 64, 64] to have 64 channels, but got 3 channels instead

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''