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
        self.conv1 = torch.nn.Conv2d(3, 12, 5, stride=2, padding=2, dilation=1)
        self.conv2 = torch.nn.Conv2d(18, 24, 5, stride=2, padding=3, dilation=1)

    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = v1 - 2.0
        v3 = F.relu(v2)
        v4 = torch.cat([x1, v3], 1)
        v5 = self.conv2(v4)
        v6 = F.relu(v5)
        v7 = torch.cat([v3, v6], 1)
        return v7



func = Model().to('cpu')


x1 = torch.randn(1, 3, 56, 56)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Sizes of tensors must match except in dimension 1. Expected size 56 but got size 28 for tensor number 1 in the list.

jit:
Failed running call_function <built-in method cat of type object at 0x731ad2d96ec0>(*([FakeTensor(..., size=(1, 3, s1, s2)), FakeTensor(..., size=(1, 12, (((s1 - 1)//2)) + 1, (((s2 - 1)//2)) + 1))], 1), **{}):
Sizes of tensors must match except in dimension 1. Expected s1 in dimension 2 but got (((s1 - 1)//2)) + 1 for tensor number 1 in the list

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''