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

    def __init__(self, min, max):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 2, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(8, 16, 2, stride=1, padding=1)
        self.min = min
        self.max = max

    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = self.conv2(v1)
        v3 = torch.clamp_min(v2, self.min)
        v4 = torch.clamp_max(v3, self.max)
        v5 = v4.permute(0, 2, 3, 1).view(100, 100, -1)
        return v5.mean(0)


min = -1.5
max = 0

func = Model(min, max).to('cpu')


x1 = torch.randn(1, 3, 64, 64)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
shape '[100, 100, -1]' is invalid for input of size 69696

jit:
Failed running call_method view(*(FakeTensor(..., size=(1, s1 + 2, s2 + 2, 16)), 100, 100, -1), **{}):
shape '[100, 100, -1]' is invalid for input of size 16*(s1 + 2)*(s2 + 2)

from user code:
   File "<string>", line 27, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''