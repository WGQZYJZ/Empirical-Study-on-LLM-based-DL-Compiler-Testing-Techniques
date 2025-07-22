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
        self.linear = torch.nn.Conv2d(32, 64, 1, stride=1, padding=1)

    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = ((v1 * torch.clamp(torch.min(v1), torch.max(v1), 6)) + 3)
        v3 = (v2 / 6)
        return v3



func = Model().to('cuda')



x1 = torch.randn(1, 3, 64, 64)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [64, 32, 1, 1], expected input[1, 3, 64, 64] to have 32 channels, but got 3 channels instead

jit:
Failed running call_module L__self___linear(*(FakeTensor(..., device='cuda:0', size=(1, 3, 64, 64)),), **{}):
Given groups=1, weight of size [64, 32, 1, 1], expected input[1, 3, 64, 64] to have 32 channels, but got 3 channels instead

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''