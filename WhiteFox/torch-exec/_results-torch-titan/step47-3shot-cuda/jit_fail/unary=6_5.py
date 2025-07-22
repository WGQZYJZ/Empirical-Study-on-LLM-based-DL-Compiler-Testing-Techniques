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
        self.conv = torch.nn.Conv2d(3, 1, 1, stride=1, padding=1)
        self.sigmoid = torch.nn.Sigmoid()
        for i in range(1000):
            self.add_module(str(i), torch.nn.Conv2d(256, 256, 1, stride=1, padding=1))

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = (v1 + 2)
        v3 = torch.clamp(v2, 0, 50)
        v4 = (v1 * v3)
        v5 = (v4 / 6)
        v6 = self.sigmoid(v5)
        for i in range(1000):
            v7 = getattr(self, str(i))(v6)
            v8 = (v7 + 2)
            v9 = torch.clamp(v8, 0, 50)
            v10 = (v7 * v9)
            v11 = (v10 / 6)
            v12 = self.sigmoid(v11)
            v6 = torch.cat((v6, v12), 1)
        return v6




func = Model().to('cuda')



x1 = torch.randn(1, 3, 64, 64)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [256, 256, 1, 1], expected input[1, 1, 66, 66] to have 256 channels, but got 1 channels instead

jit:
Failed running call_module getattr_L__self_____0__(*(FakeTensor(..., device='cuda:0', size=(1, 1, 66, 66)),), **{}):
Given groups=1, weight of size [256, 256, 1, 1], expected input[1, 1, 66, 66] to have 256 channels, but got 1 channels instead

from user code:
   File "<string>", line 32, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''