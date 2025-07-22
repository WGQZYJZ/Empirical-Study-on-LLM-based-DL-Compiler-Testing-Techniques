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
        v1 = torch.mm(x1, x1)
        v2 = torch.mm(x2, x2)
        return torch.cat([v1, v1, v2, v2], 1)



func = Model().to('cpu')


x1 = torch.randn(3, 1000)

x2 = torch.randn(1000, 4)

test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (3x1000 and 3x1000)

jit:
Failed running call_function <built-in method mm of type object at 0x7a8425396ec0>(*(FakeTensor(..., size=(3, 1000)), FakeTensor(..., size=(3, 1000))), **{}):
a and b must have same reduction dim, but got [3, 1000] X [3, 1000].

from user code:
   File "<string>", line 19, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''