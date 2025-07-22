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
        self.conv = torch.nn.Conv2d(4, 1, 3, stride=2, padding=0)

    def forward(self, x):
        v1 = self.conv(x)
        v2 = (v1 > 0)
        v3 = (v1 * (- 0.92))
        v4 = torch.where(v2, v1, v3)
        return v4




func = Model().to('cuda')



x1 = torch.randn(1, 16, 64, 16)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [1, 4, 3, 3], expected input[1, 16, 64, 16] to have 4 channels, but got 16 channels instead

jit:
Failed running call_module L__self___conv(*(FakeTensor(..., device='cuda:0', size=(1, 16, 64, 16)),), **{}):
Given groups=1, weight of size [1, 4, 3, 3], expected input[1, 16, 64, 16] to have 4 channels, but got 16 channels instead

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''