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
        self.conv1 = torch.nn.Conv2d(8, 8, 7, stride=2, padding=0)
        self.conv2 = torch.nn.Conv2d(9, 12, 5, stride=1, padding=1)

    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = v1 * 0.5
        v3 = v1 * 0.7071067811865476
        v4 = torch.erf(v3)
        v5 = v4 + 1
        v6 = v2 * v5
        v7 = torch.cat([x1, v6], 1)
        v8 = self.conv2(v7)
        return v8



func = Model().to('cpu')


x1 = torch.randn(1, 8, 202, 74)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Sizes of tensors must match except in dimension 1. Expected size 202 but got size 98 for tensor number 1 in the list.

jit:
Failed running call_function <built-in method cat of type object at 0x7c4910d96ec0>(*([FakeTensor(..., size=(1, 8, 202, 74)), FakeTensor(..., size=(1, 8, 98, 34))], 1), **{}):
Sizes of tensors must match except in dimension 1. Expected 202 in dimension 2 but got 98 for tensor number 1 in the list

from user code:
   File "<string>", line 27, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''