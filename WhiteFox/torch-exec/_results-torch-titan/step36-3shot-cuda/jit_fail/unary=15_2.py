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
        self.conv1 = torch.nn.Conv2d(64, 64, 3, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(3, 3, 1)

    def forward(self, x):
        (v0, v1) = torch.chunk(x, 2, 1)
        v2 = self.conv1(v1)
        v3 = self.conv2(x)
        return torch.cat([v2, v3], dim=1)




func = Model().to('cuda')



x = torch.randn(1, 64, 256, 256)


test_inputs = [x]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [64, 64, 3, 3], expected input[1, 32, 256, 256] to have 64 channels, but got 32 channels instead

jit:
Failed running call_module L__self___conv1(*(FakeTensor(..., device='cuda:0', size=(1, 32, 256, 256)),), **{}):
Given groups=1, weight of size [64, 64, 3, 3], expected input[1, 32, 256, 256] to have 64 channels, but got 32 channels instead

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''