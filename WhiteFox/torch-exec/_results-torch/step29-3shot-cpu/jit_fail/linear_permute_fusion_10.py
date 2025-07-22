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
        self.linear1 = torch.nn.Linear(1, 3)
        self.linear2 = torch.nn.Linear(3, 3, bias=False)

    def forward(self, x1):
        v1 = torch.nn.functional.linear(x1 + 2.0, self.linear1.weight)
        v2 = torch.nn.functional.linear(x1 + 0.5, self.linear2.weight)
        return v2



func = Model().to('cpu')


x1 = torch.randn(1, 1, 1)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (1x1 and 3x3)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., size=(1, 1, 1)), Parameter(FakeTensor(..., size=(3, 3), requires_grad=True))), **{}):
a and b must have same reduction dim, but got [1, 1] X [3, 3].

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''