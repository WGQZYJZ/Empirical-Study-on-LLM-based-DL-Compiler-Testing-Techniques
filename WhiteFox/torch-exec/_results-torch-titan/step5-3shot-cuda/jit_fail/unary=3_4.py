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
        self.conv = torch.nn.Conv2d(1, 3, 1, stride=1, padding=1)

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = (v1 * 0.7071067811865476)
        v3 = self.conv(v2)
        v4 = (v3 + 1)
        v5 = (v1 * v4)
        return v5




func = Model().to('cuda')



x1 = torch.randn(1, 1, 64, 64)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [3, 1, 1, 1], expected input[1, 3, 66, 66] to have 1 channels, but got 3 channels instead

jit:
Failed running call_module L__self___conv(*(FakeTensor(..., device='cuda:0', size=(1, 3, 66, 66)),), **{}):
Given groups=1, weight of size [3, 1, 1, 1], expected input[1, 3, 66, 66] to have 1 channels, but got 3 channels instead

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''