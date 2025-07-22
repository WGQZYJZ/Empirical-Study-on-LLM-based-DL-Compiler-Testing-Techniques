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
        v2 = v1[0][0]
        return torch.mm(v2, inp)



func = Model().to('cpu')


x1 = torch.randn(3, 3, requires_grad=True)

x2 = torch.randn(3, 3, requires_grad=True)

inp = torch.randn(3, 3)

test_inputs = [x1, x2, inp]

# JIT_FAIL
'''
direct:
self must be a matrix

jit:
Failed running call_function <built-in method mm of type object at 0x79087c996ec0>(*(FakeTensor(..., size=()), FakeTensor(..., size=(s0, s1))), **{}):
a must be 2D

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''