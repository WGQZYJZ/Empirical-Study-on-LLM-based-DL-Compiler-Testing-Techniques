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
        self.net = torch.nn.Linear(3, 8)
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x1):
        v0 = x1
        v2 = v0
        v3 = self.net(v2)
        v4 = torch.sigmoid(v3)
        v5 = v4
        v6 = self.conv(v5)
        v7 = v6
        return v7



func = Model().to('cuda')



x1 = torch.randn(1, 3, 64, 64)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (192x64 and 3x8)

jit:
Failed running call_module L__self___net(*(FakeTensor(..., device='cuda:0', size=(1, 3, 64, 64)),), **{}):
a and b must have same reduction dim, but got [192, 64] X [3, 8].

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''