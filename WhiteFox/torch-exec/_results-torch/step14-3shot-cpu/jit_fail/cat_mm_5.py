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

    def forward(self, x1, x2):
        v1 = torch.mm(x1, x2)
        v2 = torch.mm(x1, x2)
        return torch.cat([v1, v1, v1], 0)



func = Model().to('cpu')


x1 = torch.randn(3, 4)

x2 = torch.randn(2, 5)

test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (3x4 and 2x5)

jit:
Failed running call_function <built-in method mm of type object at 0x7ee98b596ec0>(*(FakeTensor(..., size=(s2, s3)), FakeTensor(..., size=(s0, s1))), **{}):
a and b must have same reduction dim, but got [s2, s3] X [s0, s1].

from user code:
   File "<string>", line 19, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''