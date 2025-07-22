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

class Model(nn.Module):

    def __init__(self):
        super().__init__()
        self.layers = nn.Linear(2, 3)

    def forward(self, x):
        t1 = torch.addmm(x, self.layers.weight, self.layers.bias)
        x = torch.stack([t1] * 3, dim=1)
        return x



func = Model().to('cpu')


x = torch.randn(2, 2)

test_inputs = [x]

# JIT_FAIL
'''
direct:
mat2 must be a matrix, got 1-D tensor

jit:
Failed running call_function <built-in method addmm of type object at 0x70804c996ec0>(*(FakeTensor(..., size=(2, 2)), Parameter(FakeTensor(..., size=(3, 2), requires_grad=True)), Parameter(FakeTensor(..., size=(3,), requires_grad=True))), **{}):
b must be 2D

from user code:
   File "<string>", line 20, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''