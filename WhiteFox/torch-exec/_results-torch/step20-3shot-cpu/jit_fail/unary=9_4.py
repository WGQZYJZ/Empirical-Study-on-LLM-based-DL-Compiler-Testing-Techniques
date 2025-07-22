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
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = 3 + v1
        v3 = v2.unsqueeze(1).min(6).squeeze(1)
        v4 = v3.unsqueeze(1).div(6).squeeze(1)
        return v4



func = Model().to('cpu')


x1 = torch.randn(1, 3, 64, 64)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Dimension out of range (expected to be in range of [-5, 4], but got 6)

jit:
Failed running call_method min(*(FakeTensor(..., size=(1, 1, 8, s1 + 2, s2 + 2)), 6), **{}):
Dimension out of range (expected to be in range of [-5, 4], but got 6)

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''