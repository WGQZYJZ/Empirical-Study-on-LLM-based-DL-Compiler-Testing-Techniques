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

    def forward(self, x1, x2, inp):
        v1 = torch.mm(x1, x2)
        v2 = v1.reshape(6, -1, 3)
        v3 = v2 * inp
        v4 = v3.permute(1, 0, 2)
        v5 = v4 + v2
        v6 = v5.permute(1, 0, 2)
        return v6



func = Model().to('cpu')


x1 = torch.randn(5, 4)

x2 = torch.randn(5, 4)

inp = torch.randn(4, 3)

test_inputs = [x1, x2, inp]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (5x4 and 5x4)

jit:
Failed running call_function <built-in method mm of type object at 0x7f3f78996ec0>(*(FakeTensor(..., size=(s2, s3)), FakeTensor(..., size=(s0, s1))), **{}):
a and b must have same reduction dim, but got [s2, s3] X [s0, s1].

from user code:
   File "<string>", line 19, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''