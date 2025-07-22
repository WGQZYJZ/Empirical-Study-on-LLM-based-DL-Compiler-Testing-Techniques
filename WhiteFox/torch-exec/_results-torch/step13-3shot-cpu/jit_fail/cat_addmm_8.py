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

    def forward(self, x1, x2, x3):
        t1 = torch.addmm(x1, x2, x3)
        t2 = torch.cat([t1], dim=1)
        return t2


func = Model().to('cpu')


x1 = torch.randn(8, 64, 16)

x2 = torch.randn(64, 128)

x3 = torch.randn(64, 128)

test_inputs = [x1, x2, x3]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (64x128 and 64x128)

jit:
Failed running call_function <built-in method addmm of type object at 0x71e598796ec0>(*(FakeTensor(..., size=(8, 64, 16)), FakeTensor(..., size=(64, 128)), FakeTensor(..., size=(64, 128))), **{}):
a and b must have same reduction dim, but got [64, 128] X [64, 128].

from user code:
   File "<string>", line 19, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''