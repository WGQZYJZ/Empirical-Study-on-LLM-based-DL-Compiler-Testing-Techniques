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
        self.conv = torch.nn.Conv2d(16, 16, 3, stride=1, padding=1)
        self.pool = torch.nn.AvgPool2d([2, 2], stride=2)

    def forward(self, x):
        v1 = self.conv(x)
        v2 = torch.flatten(v1, 1)
        v3 = torch.relu(v2)
        v4 = self.pool(v3)
        return v4




func = Model().to('cuda')



x = torch.randn(1, 16, 64, 64)


test_inputs = [x]

# JIT_FAIL
'''
direct:
Dimension out of range (expected to be in range of [-2, 1], but got -3)

jit:
Failed running call_module L__self___pool(*(FakeTensor(..., device='cuda:0', size=(1, 65536)),), **{}):
Dimension out of range (expected to be in range of [-2, 1], but got -3)

from user code:
   File "<string>", line 26, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''