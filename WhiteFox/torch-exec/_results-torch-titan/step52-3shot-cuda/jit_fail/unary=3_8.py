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
        self.conv = torch.nn.Conv2d(3, 51, 6, stride=1, padding=2)
        self.conv2 = torch.nn.Conv2d(51, 3, 6, stride=1, padding=3)
        self.conv3 = torch.nn.ConvTranspose2d(6, 51, 5, stride=3, padding=3)

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = (v1 * 0.5)
        v3 = (v1 * 0.7071067811865476)
        v4 = torch.erf(v3)
        v5 = (v4 + 1)
        v6 = (v2 * v5)
        v7 = self.conv2(v6)
        v8 = (v7 * 0.5)
        v9 = (v7 * 0.7071067811865476)
        v10 = torch.erf(v9)
        v11 = (v10 + 1)
        v12 = (v8 * v11)
        v13 = self.conv3(v12)
        return v13




func = Model().to('cuda')



x1 = torch.randn(1, 3, 35, 41)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given transposed=1, weight of size [6, 51, 5, 5], expected input[1, 3, 35, 41] to have 6 channels, but got 3 channels instead

jit:
Failed running call_module L__self___conv3(*(FakeTensor(..., device='cuda:0', size=(1, 3, 35, 41)),), **{}):
Given transposed=1, weight of size [6, 51, 5, 5], expected input[1, 3, 35, 41] to have 6 channels, but got 3 channels instead

from user code:
   File "<string>", line 36, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''