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
        self.conv1 = torch.nn.Conv2d(3, 1, 3)
        self.conv2 = torch.nn.Conv2d(3, 1, 3)
        self.bn = torch.nn.BatchNorm2d(3)
        self.relu = torch.nn.ReLU()

    def forward(self, x1, x2):
        x = torch.cat((x1, x2), 1)
        x = self.conv1(x)
        x = self.relu(x)
        x = self.conv2(x)
        y = x + self.bn(x)
        return y



func = Model().to('cpu')


x1 = torch.randn(1, 3, 6, 6)

x2 = torch.randn(1, 3, 2, 2)

test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
Sizes of tensors must match except in dimension 1. Expected size 6 but got size 2 for tensor number 1 in the list.

jit:
Failed running call_function <built-in method cat of type object at 0x78f363d96ec0>(*((FakeTensor(..., size=(1, 3, 6, 6)), FakeTensor(..., size=(1, 3, 2, 2))), 1), **{}):
Sizes of tensors must match except in dimension 1. Expected 6 in dimension 2 but got 2 for tensor number 1 in the list

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''