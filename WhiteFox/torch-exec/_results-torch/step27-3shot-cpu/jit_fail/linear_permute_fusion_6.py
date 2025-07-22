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
        self.linear1 = torch.nn.Linear(2, 2)
        self.linear2 = torch.nn.Linear(3, 3)

    def forward(self, x1):
        v1 = torch.nn.functional.linear(x1, self.linear1.weight, self.linear1.bias)
        v2 = v1.permute(0, 2, 1, 3)
        y = (v2 * self.linear2.weight.unsqueeze(0)).sum([0, 1, 2])
        return v1



func = Model().to('cpu')


x1 = torch.randn(2, 2, 3, device='cpu')

test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (4x3 and 2x2)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., size=(s0, 2, s1)), Parameter(FakeTensor(..., size=(2, 2), requires_grad=True)), Parameter(FakeTensor(..., size=(2,), requires_grad=True))), **{}):
a and b must have same reduction dim, but got [2*s0, s1] X [2, 2].

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''