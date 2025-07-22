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
        self.conv1 = torch.nn.Conv2d(in_channels=3, out_channels=48, kernel_size=3, stride=1, padding=1)

    def forward(self, x1, x2, x3):
        v1 = torch.sigmoid(self.conv1(x1))
        v2 = torch.softmax(v1, 1)
        v3 = v2 + 1.0
        v4 = torch.sigmoid(v2)
        m1 = torch.stack([v3, v4], 0)
        v5 = self.conv1(x2)
        v6 = torch.sigmoid(v5)
        v7 = torch.cat([m1, v6], 1)
        m2 = torch.sigmoid(v7)
        v8 = torch.cat([m2, x3], 1)
        return v8



func = Model().to('cpu')


x1 = torch.randn(3, 3, 107, 107)

x2 = torch.randn(3, 3, 53, 53)

x3 = torch.randn(3, 3, 31, 31)

test_inputs = [x1, x2, x3]

# JIT_FAIL
'''
direct:
Tensors must have same number of dimensions: got 5 and 4

jit:
Failed running call_function <built-in method cat of type object at 0x73d997f96ec0>(*([FakeTensor(..., size=(2, 3, 48, s0, s1)), FakeTensor(..., size=(3, 48, 53, 53))], 1), **{}):
Number of dimensions of tensors must match.  Expected 5-D tensors, but got 4-D for tensor number 1 in the list

from user code:
   File "<string>", line 27, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''