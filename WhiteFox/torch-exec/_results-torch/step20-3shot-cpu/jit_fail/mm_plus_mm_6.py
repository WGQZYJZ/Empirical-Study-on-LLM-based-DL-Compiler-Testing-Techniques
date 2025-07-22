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

class Model(nn.Module):

    def forward(self, x1, x2, x3, x4):
        v1 = torch.mm(x1, x1)
        v2 = x2.mm(x2)
        v3 = torch.mm(x3, x2)
        v4 = x4.mm(x3)
        return v1 * v2 + v3 + v4



func = Model().to('cpu')


x1 = torch.randn(100, 55)

x2 = torch.randn(55, 100)

x3 = torch.randn(100, 55)

x4 = torch.randn(55, 100)

test_inputs = [x1, x2, x3, x4]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (100x55 and 100x55)

jit:
Failed running call_function <built-in method mm of type object at 0x754b36996ec0>(*(FakeTensor(..., size=(100, 55)), FakeTensor(..., size=(100, 55))), **{}):
a and b must have same reduction dim, but got [100, 55] X [100, 55].

from user code:
   File "<string>", line 16, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''