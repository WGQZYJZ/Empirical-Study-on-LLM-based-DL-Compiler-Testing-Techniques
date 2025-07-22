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
        self.linear = torch.nn.Linear(5, 2)

    def forward(self, x1):
        v1 = torch.nn.functional.linear(x1, self.linear.weight, self.linear.bias)
        v2 = v1
        v3 = v1
        v4 = v2 + v1
        v5 = v4
        v6 = v4
        v7 = v4 / v6
        v8 = v4
        v9 = v4
        v10 = v9
        v11 = v6 + v10
        v12 = v5 + v11
        v13 = v11
        v14 = v12 + v13
        return v11



func = Model().to('cpu')


x1 = torch.randn(1, 5, 2)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (5x2 and 5x2)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., size=(1, s0, 2)), Parameter(FakeTensor(..., size=(2, 5), requires_grad=True)), Parameter(FakeTensor(..., size=(2,), requires_grad=True))), **{}):
a and b must have same reduction dim, but got [s0, 2] X [5, 2].

from user code:
   File "<string>", line 20, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''