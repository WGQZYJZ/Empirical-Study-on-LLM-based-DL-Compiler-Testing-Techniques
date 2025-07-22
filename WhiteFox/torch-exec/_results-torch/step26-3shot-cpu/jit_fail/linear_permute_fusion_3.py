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
        self.linear = torch.nn.Linear(1, 2)

    def forward(self, x1, x2):
        t = torch.cat([x1, x2], dim=1)
        v1 = torch.nn.functional.linear(t, self.linear.weight, self.linear.bias)
        k = v1.permute(0, 2, 1)
        return k



func = Model().to('cpu')


x1 = torch.randn(3, 1)

x2 = torch.randn(3, 1)

test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (3x2 and 1x2)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., size=(3, 2)), Parameter(FakeTensor(..., size=(2, 1), requires_grad=True)), Parameter(FakeTensor(..., size=(2,), requires_grad=True))), **{}):
a and b must have same reduction dim, but got [3, 2] X [1, 2].

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''