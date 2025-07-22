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
        self.conv1 = torch.nn.Conv2d(1, 8, 45, stride=1, padding=22)
        self.conv2 = torch.nn.Conv2d(8, 8, 3, stride=1, padding=0)
        self.conv3 = torch.nn.Conv2d(8, 8, 1, stride=1, padding=1)

    def forward(self, x1):
        v1 = torch.nn.functional.conv2d(x1, self.conv1.weight, self.conv1.bias, -18, 5, 22, 1)
        v2 = v1 * 0.5
        v3 = v1 * 0.7071067811865476
        v4 = torch.erf(v3)
        v5 = v4 + 1
        v6 = v2 * v5
        v7 = torch.nn.functional.conv2d(v6, self.conv2.weight, self.conv2.bias, 10, 1, 0)
        v8 = torch.nn.functional.conv2d(v7, self.conv3.weight, self.conv3.bias, 1, 5, 1, 0)
        v9 = v8 * 0.5
        v10 = v8 * 0.7071067811865476
        v11 = torch.erf(v10)
        v12 = v11 + 1
        v13 = v9 * v12
        return v13



func = Model().to('cpu')


x1 = torch.randn(1, 1, 112, 137)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
non-positive stride is not supported

jit:
Failed running call_function <built-in method conv2d of type object at 0x7bec1f396ec0>(*(FakeTensor(..., size=(1, 1, s0, s1)), Parameter(FakeTensor(..., size=(8, 1, 45, 45), requires_grad=True)), Parameter(FakeTensor(..., size=(8,), requires_grad=True)), -18, 5, 22, 1), **{}):
non-positive stride is not supported

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''