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
        super(Model, self).__init__()
        self.conv1 = torch.nn.Conv2d(512, 128, 3, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(128, 64, 3, stride=1, padding=1)
        self.conv3 = torch.nn.Conv2d(64, 32, 3, stride=1, padding=1)
        self.pool = torch.nn.AvgPool2d(2)

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
        v19 = self.pool(v18)
        return v19




func = Model().to('cuda')



x1 = torch.randn(1, 256, 60, 60)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [128, 512, 3, 3], expected input[1, 256, 60, 60] to have 512 channels, but got 256 channels instead

jit:
Failed running call_module L__self___conv1(*(FakeTensor(..., device='cuda:0', size=(1, 256, 60, 60)),), **{}):
Given groups=1, weight of size [128, 512, 3, 3], expected input[1, 256, 60, 60] to have 512 channels, but got 256 channels instead

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''