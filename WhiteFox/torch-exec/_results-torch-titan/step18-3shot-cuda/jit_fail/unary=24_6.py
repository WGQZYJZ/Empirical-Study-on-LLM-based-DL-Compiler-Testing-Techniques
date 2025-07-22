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
        self.conv = torch.nn.Conv2d(8, 16, 5, stride=1, padding=1)

    def forward(self, x):
        v1 = self.conv(x)
        v2 = (v1 > 0)
        v3 = (v1 * 0.2)
        v4 = torch.where(v2, v1, v3)
        return v4




func = Model().to('cuda')



x1 = torch.randn(9, 2, 64, 64)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [16, 8, 5, 5], expected input[9, 2, 64, 64] to have 8 channels, but got 2 channels instead

jit:
Failed running call_module L__self___conv(*(FakeTensor(..., device='cuda:0', size=(9, 2, 64, 64)),), **{}):
Given groups=1, weight of size [16, 8, 5, 5], expected input[9, 2, 64, 64] to have 8 channels, but got 2 channels instead

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''