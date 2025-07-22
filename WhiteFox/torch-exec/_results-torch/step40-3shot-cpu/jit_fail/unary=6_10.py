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
        self.conv = torch.nn.Conv2d(3, 6, 1, stride=1, padding=0)
        self.avgpool = torch.nn.AdaptiveAvgPool2d((1, 6))

    def forward(self, x1):
        t1 = self.conv(x1)
        t2 = t1 + 3
        t4 = torch.clamp_min(t2, 0)
        t5 = torch.clamp_max(t4, 6)
        t6 = self.avgpool(x1).squeeze(-1)
        t7 = t6 * t5
        t8 = t7 / 6
        return t8



func = Model().to('cpu')


x1 = torch.randn(2, 3, 64, 64)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
The size of tensor a (6) must match the size of tensor b (64) at non-singleton dimension 3

jit:
Failed running call_function <built-in function mul>(*(FakeTensor(..., size=(s0, 3, 1, 6)), FakeTensor(..., size=(s0, 6, s2, s3))), **{}):
The size of tensor a (6) must match the size of tensor b (s3) at non-singleton dimension 3)

from user code:
   File "<string>", line 26, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''