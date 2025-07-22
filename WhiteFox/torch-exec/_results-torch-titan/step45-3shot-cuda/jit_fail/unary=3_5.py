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
        self.conv1 = torch.nn.Conv2d(90, 256, 8, stride=1, padding=0)
        self.conv2 = torch.nn.Conv2d(256, 256, 9, stride=2, padding=0)
        self.conv3 = torch.nn.Conv2d(256, 256, 3, stride=1, padding=1)
        self.conv4 = torch.nn.Conv2d(256, 256, 7, stride=1, padding=0)

    def forward(self, x1):
        v1 = self.conv1(x1)
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
        v14 = (v13 * 0.5)
        v15 = (v13 * 0.7071067811865476)
        v16 = torch.erf(v15)
        v17 = (v16 + 1)
        v18 = (v14 * v17)
        v19 = self.conv4(v18)
        return v19




func = Model().to('cuda')



x1 = torch.randn(1, 90, 17, 39)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Calculated padded input size per channel: (1 x 12). Kernel size: (7 x 7). Kernel size can't be greater than actual input size

jit:
Failed running call_module L__self___conv4(*(FakeTensor(..., device='cuda:0', size=(1, 256, 1, 12)),), **{}):
Calculated padded input size per channel: (1 x 12). Kernel size: (7 x 7). Kernel size can't be greater than actual input size

from user code:
   File "<string>", line 43, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''