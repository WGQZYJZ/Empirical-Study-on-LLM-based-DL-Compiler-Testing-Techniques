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

    def forward(self, x, y):
        v1 = torch.transpose(x, 0, 1)
        v2 = torch.mm(v1, v1)
        return v2 if (v1 > v2).all() else v1



func = Model().to('cpu')


x = torch.randn(1, 5)

y = torch.randn(1, 5)

test_inputs = [x, y]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (5x1 and 5x1)

jit:
Failed running call_function <built-in method mm of type object at 0x7bc76a196ec0>(*(FakeTensor(..., size=(5, 1)), FakeTensor(..., size=(5, 1))), **{}):
a and b must have same reduction dim, but got [5, 1] X [5, 1].

from user code:
   File "<string>", line 20, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''