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

    def forward(self, x):
        x1 = torch.matmul(x, x)
        t = x + x1
        return t



func = Model().to('cpu')


x = torch.randn(12, 1, requires_grad=True)

test_inputs = [x]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (12x1 and 12x1)

jit:
Failed running call_function <built-in method matmul of type object at 0x76dae6d96ec0>(*(FakeTensor(..., size=(12, 1)), FakeTensor(..., size=(12, 1))), **{}):
a and b must have same reduction dim, but got [12, 1] X [12, 1].

from user code:
   File "<string>", line 19, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''