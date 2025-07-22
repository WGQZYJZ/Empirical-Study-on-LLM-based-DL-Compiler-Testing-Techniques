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
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1.transpose(1, 2)
        v3 = v2.div(2)
        v4 = (v3 - 2.1).abs()
        v5 = torch.clamp(v4, min=0.1)
        v6 = torch.clamp(v5, max=0.9)
        v7 = v6.transpose(2, 1)
        return v7




func = Model().to('cuda')



x1 = torch.randn(1, 6, 64, 64)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [8, 3, 1, 1], expected input[1, 6, 64, 64] to have 3 channels, but got 6 channels instead

jit:
Failed running call_module L__self___conv(*(FakeTensor(..., device='cuda:0', size=(1, 6, 64, 64)),), **{}):
Given groups=1, weight of size [8, 3, 1, 1], expected input[1, 6, 64, 64] to have 3 channels, but got 6 channels instead

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''