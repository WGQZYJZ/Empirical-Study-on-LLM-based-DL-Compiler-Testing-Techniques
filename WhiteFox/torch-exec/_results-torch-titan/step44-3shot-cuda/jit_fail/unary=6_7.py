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
        self.conv2d = torch.nn.Conv2d(3, 6, 1, stride=1, padding=1)

    def forward(self, x):
        v3 = self.conv2d(x)
        v6 = self.conv2d(v3)
        v1 = (3 + v3)
        v2 = torch.clamp(v1, 0, 6)
        v5 = (v2 * v6)
        v4 = (v5 / 6)
        return v4




func = Model().to('cuda')



x1 = torch.randn(1, 3, 64, 64)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [6, 3, 1, 1], expected input[1, 6, 66, 66] to have 3 channels, but got 6 channels instead

jit:
Failed running call_module L__self___conv2d(*(FakeTensor(..., device='cuda:0', size=(1, 6, 66, 66)),), **{}):
Given groups=1, weight of size [6, 3, 1, 1], expected input[1, 6, 66, 66] to have 3 channels, but got 6 channels instead

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''