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
        t = [v1] * 50
        return torch.cat(t, 1)



func = Model().to('cpu')


x1 = torch.randn(1, 5)

x2 = torch.randn(1, 4)

test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (1x5 and 1x4)

jit:
Failed running call_function <built-in method mm of type object at 0x724060d96ec0>(*(FakeTensor(..., size=(1, s1)), FakeTensor(..., size=(1, s0))), **{}):
a and b must have same reduction dim, but got [1, s1] X [1, s0].

from user code:
   File "<string>", line 19, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''