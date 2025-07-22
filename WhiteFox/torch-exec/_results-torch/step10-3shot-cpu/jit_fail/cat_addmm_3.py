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
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x1):
        v1 = torch.addmm(x1, torch.ones((1, 3, 64, 64)), torch.ones((64, 3, 1, 1)))
        return v1


func = Model().to('cpu')


x1 = torch.randn(1, 3, 64, 64)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 must be a matrix, got 4-D tensor

jit:
Failed running call_function <built-in method addmm of type object at 0x71ddb4396ec0>(*(FakeTensor(..., size=(1, s0, s1, s2)), FakeTensor(..., size=(1, 3, 64, 64)), FakeTensor(..., size=(64, 3, 1, 1))), **{}):
a must be 2D

from user code:
   File "<string>", line 20, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''