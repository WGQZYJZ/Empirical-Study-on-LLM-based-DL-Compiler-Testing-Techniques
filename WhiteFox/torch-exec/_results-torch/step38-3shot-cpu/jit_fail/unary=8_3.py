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
        self.conv_transpose = torch.nn.ConvTranspose2d(128, 32, 3, stride=1)

    def forward(self, x1, x2, x3):
        v1 = self.conv_transpose(x1)
        v2 = v1.flatten(2)
        v3 = v2 / x3.flatten(2).sum((2, 3))
        v4 = v2 + v3
        return v4



func = Model().to('cpu')


x1 = torch.randn(1, 128, 100, 150)

x2 = torch.randn(1, 100, 1)

x3 = torch.randn(1, 100)

test_inputs = [x1, x2, x3]

# JIT_FAIL
'''
direct:
Dimension out of range (expected to be in range of [-2, 1], but got 2)

jit:
Failed running call_method flatten(*(FakeTensor(..., size=(1, 100)), 2), **{}):
Dimension out of range (expected to be in range of [-2, 1], but got 2)

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''