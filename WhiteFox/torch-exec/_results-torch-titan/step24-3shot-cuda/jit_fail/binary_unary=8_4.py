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
        self.conv = torch.nn.Conv2d(1, 8, 2, stride=2, padding=0)
        self.linear = torch.nn.Linear(8, 16)

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = self.conv(v1)
        v3 = v2.flatten(start_dim=1)
        v4 = self.linear(v3)
        return v4




func = Model().to('cuda')



x1 = torch.randn(1, 1, 64, 64)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [8, 1, 2, 2], expected input[1, 8, 32, 32] to have 1 channels, but got 8 channels instead

jit:
Failed running call_module L__self___conv(*(FakeTensor(..., device='cuda:0', size=(1, 8, 32, 32)),), **{}):
Given groups=1, weight of size [8, 1, 2, 2], expected input[1, 8, 32, 32] to have 1 channels, but got 8 channels instead

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''