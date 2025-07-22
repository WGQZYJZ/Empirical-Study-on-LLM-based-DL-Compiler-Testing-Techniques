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
        self.weight = torch.nn.Parameter(torch.randn(2, 3))
        self.bias = torch.nn.Parameter(torch.randn(3))

    def forward(self, x0):
        v0 = torch.nn.functional.linear(x0, self.weight, self.bias)
        v1 = v0.permute(0, 2, 1)
        return v1



func = Model().to('cpu')


x0 = torch.randn(1, 2, 2, 2)

test_inputs = [x0]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (4x2 and 3x2)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., size=(1, 2, 2, 2)), Parameter(FakeTensor(..., size=(2, 3), requires_grad=True)), Parameter(FakeTensor(..., size=(3,), requires_grad=True))), **{}):
a and b must have same reduction dim, but got [4, 2] X [3, 2].

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''