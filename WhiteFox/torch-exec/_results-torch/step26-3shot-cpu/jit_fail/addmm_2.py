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
        t1 = torch.mm(x2, inp)
        t2 = t1.repeat(1, 3)
        t3 = torch.mm(t2, t2)
        t4 = torch.mm(t3, x2)
        return x2 + t4



func = Model().to('cpu')


x1 = torch.randn(3, 3)

x2 = torch.randn(3, 3)

inp = torch.randn(3, 3)

test_inputs = [x1, x2, inp]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (3x9 and 3x9)

jit:
Failed running call_function <built-in method mm of type object at 0x74e6adb96ec0>(*(FakeTensor(..., size=(3, 9)), FakeTensor(..., size=(3, 9))), **{}):
a and b must have same reduction dim, but got [3, 9] X [3, 9].

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''