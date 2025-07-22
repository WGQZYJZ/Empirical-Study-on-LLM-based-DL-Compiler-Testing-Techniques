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
        self.t1 = torch.nn.Parameter(torch.tensor(2.0))

    def forward(self, x1, x2, inp):
        v1 = torch.nn.ReLU()(torch.mm(x1, self.t1))
        v2 = torch.nn.Sigmoid()(torch.mm(x2, inp))
        return torch.mm(v1, v2)



func = Model().to('cpu')


x1 = torch.randn(3, 3)

x2 = torch.randn(3, 3)

inp = torch.randn(3, 3)

test_inputs = [x1, x2, inp]

# JIT_FAIL
'''
direct:
mat2 must be a matrix

jit:
Failed running call_function <built-in method mm of type object at 0x7f2384f96ec0>(*(FakeTensor(..., size=(3, 3)), Parameter(FakeTensor(..., size=(), requires_grad=True))), **{}):
b must be 2D

from user code:
   File "<string>", line 20, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''