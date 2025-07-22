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
        self.conv1 = torch.nn.Conv2d(256, 256, 1, stride=1, padding=0)
        self.conv2 = torch.nn.Conv2d(256, 256, 3, stride=1, padding=1)
        self.conv3 = torch.nn.Conv2d(256, int((256 / 2)), 1, stride=1, padding=1)
        self.conv4 = torch.nn.Conv2d(int((256 / 2)), 256, 1, stride=1, padding=1)

    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = (v1 * 0.7071067811865476)
        v3 = torch.erf(v2)
        v4 = (v3 + 1)
        v5 = self.conv2(v4)
        v6 = (v5 * 0.5)
        v7 = (v5 * 0.7071067811865476)
        v8 = torch.erf(v7)
        v9 = (v8 + 1)
        v10 = self.conv3(v9)
        v11 = (v5 * 0.5)
        v12 = (v5 * 0.7071067811865476)
        v13 = torch.erf(v12)
        v14 = (v13 + 1)
        v15 = self.conv4(v14)
        return v15




func = Model().to('cuda')



x1 = torch.randn(16, 256, 16, 16)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [256, 128, 1, 1], expected input[16, 256, 16, 16] to have 128 channels, but got 256 channels instead

jit:
Failed running call_module L__self___conv4(*(FakeTensor(..., device='cuda:0', size=(16, 256, 16, 16)),), **{}):
Given groups=1, weight of size [256, 128, 1, 1], expected input[16, 256, 16, 16] to have 128 channels, but got 256 channels instead

from user code:
   File "<string>", line 39, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''