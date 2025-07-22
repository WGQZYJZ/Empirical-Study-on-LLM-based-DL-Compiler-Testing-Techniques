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
        self.conv_1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.conv_2 = torch.nn.Conv2d(8, 8, 1, stride=1, padding=1)

    def forward(self, x1):
        v1 = 3 + self.conv_1(x1)
        v2 = v1.clamp_(0, 5)
        v3 = v2.div(6)
        v4 = v3.reshape(1, 8, 64, 64)
        v5 = self.conv_2(v4)
        v6 = v5.abs()
        return v6



func = Model().to('cpu')


x1 = torch.randn(1, 3, 64, 64)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
shape '[1, 8, 64, 64]' is invalid for input of size 34848

jit:
Failed running call_method reshape(*(FakeTensor(..., size=(1, 8, 66, 66)), 1, 8, 64, 64), **{}):
shape '[1, 8, 64, 64]' is invalid for input of size 34848

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''