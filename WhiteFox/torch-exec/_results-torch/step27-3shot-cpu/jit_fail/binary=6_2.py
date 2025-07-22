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
        super(Model, self).__init__()
        self.line = torch.nn.Linear(12, 21)

    def forward(self, x1, x2):
        v0 = torch.ones(1, 1)
        v1 = torch.matmul(v0, x1.transpose(0, 1)).transpose(0, 1)
        v2 = v0 * v1
        v3 = v2.flatten()
        v4 = torch.matmul(v3, x2) + 5
        v5 = torch.tanh(v4)
        v6 = v5.sum()
        return v6


func = Model().to('cpu')


x1 = torch.randn(1, 12)

x2 = torch.randn(12)

test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (1x1 and 12x1)

jit:
Failed running call_function <built-in method matmul of type object at 0x77fae9596ec0>(*(FakeTensor(..., size=(1, 1)), FakeTensor(..., size=(s0, 1))), **{}):
a and b must have same reduction dim, but got [1, 1] X [s0, 1].

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''