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
        self.linear1 = torch.nn.Linear(1, 3, bias=False)
        self.linear2 = torch.nn.Linear(3, 1)

    def forward(self, x1):
        v1 = torch.nn.functional.linear(x1, self.linear1.weight)
        v2 = v1.permute(0, 2, 1)
        v3 = torch.nn.functional.linear(v1, self.linear2.weight)
        return v3



func = Model().to('cpu')


x1 = torch.randn(2, 3, 3)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (6x3 and 1x3)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., size=(s0, s1, s2)), Parameter(FakeTensor(..., size=(3, 1), requires_grad=True))), **{}):
a and b must have same reduction dim, but got [s0*s1, s2] X [1, 3].

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''