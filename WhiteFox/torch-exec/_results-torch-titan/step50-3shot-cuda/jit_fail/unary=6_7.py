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
        self.avgpool = torch.nn.AvgPool2d(3, stride=1, padding=1)
        self.fc1 = torch.nn.Linear(32, 16)
        self.fc2 = torch.nn.Linear(16, 32)

    def forward(self, x1):
        t1 = self.avgpool(x1)
        v2 = t1.view(t1.size(0), (- 1))
        v3 = self.fc1(v2)
        v4 = (3 + v3)
        v5 = torch.clamp_min(v4, 0)
        v6 = torch.clamp_max(v5, 6)
        v7 = (v3 * v6)
        v8 = (v6 / 6)
        v9 = self.fc2(v8)
        return v9




func = Model().to('cuda')



x1 = torch.randn(2, 3, 64, 64)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (2x12288 and 32x16)

jit:
Failed running call_module L__self___fc1(*(FakeTensor(..., device='cuda:0', size=(2, 12288)),), **{}):
a and b must have same reduction dim, but got [2, 12288] X [32, 16].

from user code:
   File "<string>", line 26, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''