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

    def forward(self, x1, x2, x3, x4):
        v1 = torch.mm(x1, x2)
        v2 = torch.mm(x3, x1)
        v3 = v1 + v2
        return v3



func = Model().to('cpu')


x1 = torch.randn(4, 3)

x2 = torch.randn(3, 4)

x3 = torch.randn(4, 3)

x4 = torch.randn(4, 3)

test_inputs = [x1, x2, x3, x4]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (4x3 and 4x3)

jit:
Failed running call_function <built-in method mm of type object at 0x7adb96196ec0>(*(FakeTensor(..., size=(s4, s5)), FakeTensor(..., size=(s2, s0))), **{}):
a and b must have same reduction dim, but got [s4, s5] X [s2, s0].

from user code:
   File "<string>", line 17, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''