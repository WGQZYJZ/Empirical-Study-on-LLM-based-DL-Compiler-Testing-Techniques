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

    def forward(self, x2):
        t = torch.randn(1, 0)
        v1 = torch.mm(x2 + t, t)
        v2 = torch.mm(v1, t)
        v3 = torch.mm(v1, x2)
        v4 = v3 + v2
        return v4



func = Model().to('cpu')


x2 = torch.randn(1, 1)

test_inputs = [x2]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (1x0 and 1x0)

jit:
Failed running call_function <built-in method mm of type object at 0x77317d596ec0>(*(FakeTensor(..., size=(1, 0)), FakeTensor(..., size=(1, 0))), **{}):
a and b must have same reduction dim, but got [1, 0] X [1, 0].

from user code:
   File "<string>", line 20, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''