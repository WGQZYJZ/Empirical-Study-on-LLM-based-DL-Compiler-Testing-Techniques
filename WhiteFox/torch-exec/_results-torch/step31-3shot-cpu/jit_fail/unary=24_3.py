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
        negative_slope = 0.1
        self.conv_1 = torch.nn.Conv2d(16, 16, 3, stride=1, padding=1)
        self.conv_2 = torch.nn.Conv2d(16, 16, 3, stride=1, padding=1)

    def forward(self, x):
        v1 = self.conv_1(x)
        v2 = v1 > 0
        v3 = v1 * negative_slope
        v4 = torch.where(v2, v1, v3)
        v5 = self.conv_2(v4)
        return v5



func = Model().to('cpu')


x1 = torch.randn(1, 16, 64, 64)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
name 'negative_slope' is not defined

jit:
NameError: name 'negative_slope' is not defined

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''