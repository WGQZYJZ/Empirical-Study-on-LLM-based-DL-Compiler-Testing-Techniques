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
        self.conv = torch.nn.Conv2d(3, 3, 3)
        self.bn = torch.nn.BatchNorm2d(3)

    def forward(self, x1, x2):
        x1 = self.conv(x1)
        x2 = self.bn(x2)
        return torch.cat(4 * [x1, x2], 1)



func = Model().to('cpu')


x1 = torch.randn(1, 3, 4, 4)

x2 = torch.randn(1, 3, 4, 4)

test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
Sizes of tensors must match except in dimension 1. Expected size 2 but got size 4 for tensor number 1 in the list.

jit:
Failed running call_function <built-in method cat of type object at 0x75431a596ec0>(*([FakeTensor(..., size=(1, 3, 2, 2)), FakeTensor(..., size=(1, 3, s0, s1)), FakeTensor(..., size=(1, 3, 2, 2)), FakeTensor(..., size=(1, 3, s0, s1)), FakeTensor(..., size=(1, 3, 2, 2)), FakeTensor(..., size=(1, 3, s0, s1)), FakeTensor(..., size=(1, 3, 2, 2)), FakeTensor(..., size=(1, 3, s0, s1))], 1), **{}):
Sizes of tensors must match except in dimension 1. Expected 2 in dimension 2 but got s0 for tensor number 1 in the list

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''