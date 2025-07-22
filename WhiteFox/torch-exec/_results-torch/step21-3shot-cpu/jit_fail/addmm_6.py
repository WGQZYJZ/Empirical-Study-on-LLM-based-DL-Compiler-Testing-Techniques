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
        v1 = inp + x2
        v2 = torch.mm(x1, inp)
        v3 = (v1 + inp) * v2 + v2
        return v3



func = Model().to('cpu')


x1 = torch.randn(3, 5)

x2 = torch.randn(5)

inp = torch.randn(5, 5, 5, 5)

test_inputs = [x1, x2, inp]

# JIT_FAIL
'''
direct:
mat2 must be a matrix

jit:
Failed running call_function <built-in method mm of type object at 0x742872b96ec0>(*(FakeTensor(..., size=(s5, s6)), FakeTensor(..., size=(s0, s1, s2, s3))), **{}):
b must be 2D

from user code:
   File "<string>", line 20, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''