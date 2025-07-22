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
        self.conv = torch.nn.Conv2d(1, 3, 1, stride=2, padding=0)
        self.conv2 = torch.nn.Conv2d(3, 3, 3, stride=2, padding=1)
        self.conv3 = torch.nn.Conv2d(3, 3, 5, stride=2, padding=2)
        self.conv4 = torch.nn.Conv2d(3, 3, 7, stride=2, padding=3)
        self.conv5 = torch.nn.Conv2d(3, 3, 7, stride=2, padding=0)

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = (v1 * 0.5)
        v3 = (v1 * 0.7071067811865476)
        v4 = torch.erf(v3)
        v5 = (v4 + 1)
        v6 = (v2 * v5)
        v7 = self.conv2(v6)
        v8 = self.conv3(v7)
        v9 = (v8 * 0.5)
        v10 = (v8 * 0.7071067811865476)
        v11 = torch.erf(v10)
        v12 = (v11 + 1)
        v13 = (v9 * v12)
        v14 = self.conv4(v13)
        v15 = self.conv5(v14)
        return v15




func = Model().to('cuda')



x1 = torch.randn(1, 512, 14, 14)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [3, 1, 1, 1], expected input[1, 512, 14, 14] to have 1 channels, but got 512 channels instead

jit:
Failed running call_module L__self___conv(*(FakeTensor(..., device='cuda:0', size=(1, 512, 14, 14)),), **{}):
Given groups=1, weight of size [3, 1, 1, 1], expected input[1, 512, 14, 14] to have 1 channels, but got 512 channels instead

from user code:
   File "<string>", line 26, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''