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
        self.linear1 = torch.nn.Linear(3, 3, bias=False)
        self.linear2 = torch.nn.Linear(3, 1, bias=False)

    def forward(self, x1, x2, inp):
        v1 = self.linear2(torch.mm(self.linear1(x1), x2))
        v2 = v1 + inp
        return torch.mm(v2, inp)



func = Model().to('cpu')


x1 = torch.randn(3, 3)

x2 = torch.randn(3, 3)

inp = torch.randn(3, 3, 3)

test_inputs = [x1, x2, inp]

# JIT_FAIL
'''
direct:
self must be a matrix

jit:
Failed running call_function <built-in method mm of type object at 0x7f8b6a996ec0>(*(FakeTensor(..., size=(s0, 3, s2)), FakeTensor(..., size=(s0, 3, s2))), **{}):
a must be 2D

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''