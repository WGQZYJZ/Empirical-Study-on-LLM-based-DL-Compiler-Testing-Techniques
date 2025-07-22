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
        self.conv1 = torch.nn.Conv2d(3, 3, 1, stride=1, padding=1, dilation=1)
        self.conv2 = torch.nn.Conv2d(3, 3, 5, stride=1, padding=2, dilation=2)

    def forward(self, x):
        v1 = self.conv1(x)
        v2 = self.conv2(x)
        v3 = v1 > 0
        v4 = v2 > 0
        v5 = v1 * 0.1
        v7 = v2 * 0.1
        v6 = torch.cat((v1, v2, -v1, -v2), 0)
        v8 = torch.cat((v5, v7), 0)
        v9 = torch.cat((v6, v8), 1)
        v10 = torch.where(v3, v5, v7)
        v11 = torch.where(v4, v9, v10)
        return v11



func = Model().to('cpu')


x1 = torch.randn(1, 3, 32, 32)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Sizes of tensors must match except in dimension 0. Expected size 34 but got size 28 for tensor number 1 in the list.

jit:
Failed running call_function <built-in method cat of type object at 0x747c1a396ec0>(*((FakeTensor(..., size=(1, 3, 34, 34)), FakeTensor(..., size=(1, 3, 28, 28)), FakeTensor(..., size=(1, 3, 34, 34)), FakeTensor(..., size=(1, 3, 28, 28))), 0), **{}):
Sizes of tensors must match except in dimension 0. Expected 34 in dimension 2 but got 28 for tensor number 1 in the list

from user code:
   File "<string>", line 27, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''