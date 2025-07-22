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
        self.linear_layer1 = torch.nn.Linear(10, 10)

    def forward(self, x1, x2, x3, x4):
        v1 = torch.mm(x1, x2)
        v2 = torch.mm(x3, x4)
        v3 = v1 + self.linear_layer1(v2)
        return v3



func = Model().to('cpu')


x1 = torch.randn(1, 10)

x2 = torch.randn(1, 10)

x3 = torch.randn(1, 10)

x4 = torch.randn(1, 10)

test_inputs = [x1, x2, x3, x4]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (1x10 and 1x10)

jit:
Failed running call_function <built-in method mm of type object at 0x742670196ec0>(*(FakeTensor(..., size=(1, s1)), FakeTensor(..., size=(1, s0))), **{}):
a and b must have same reduction dim, but got [1, s1] X [1, s0].

from user code:
   File "<string>", line 20, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''