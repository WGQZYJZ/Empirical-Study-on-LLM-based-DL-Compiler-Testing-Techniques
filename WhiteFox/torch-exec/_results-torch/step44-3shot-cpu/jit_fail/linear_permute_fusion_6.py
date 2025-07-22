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
        self.linear1 = torch.nn.Linear(6, 2)
        self.linear2 = torch.nn.Linear(3, 2)

    def forward(self, x):
        v1 = torch.nn.functional.linear(x, self.linear1.weight, self.linear1.bias)
        v2 = torch.nn.functional.linear(x, self.linear2.weight, self.linear2.bias)
        return torch.cat([v1, v2])



func = Model().to('cpu')


x = torch.randn(1, 6)

test_inputs = [x]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (1x6 and 3x2)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., size=(1, 6)), Parameter(FakeTensor(..., size=(2, 3), requires_grad=True)), Parameter(FakeTensor(..., size=(2,), requires_grad=True))), **{}):
a and b must have same reduction dim, but got [1, 6] X [3, 2].

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''