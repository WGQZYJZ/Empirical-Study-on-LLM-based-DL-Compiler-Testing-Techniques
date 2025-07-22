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
        self.weight = torch.nn.Parameter(torch.ones(3))

    def forward(self, x1):
        v1 = self.weight * x1
        return v1



func = Model().to('cpu')


x1 = torch.randn(1, 3, 64, 64)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
The size of tensor a (3) must match the size of tensor b (64) at non-singleton dimension 3

jit:
Failed running call_function <built-in function mul>(*(Parameter(FakeTensor(..., size=(3,), requires_grad=True)), FakeTensor(..., size=(1, s0, s1, s2))), **{}):
The size of tensor a (3) must match the size of tensor b (s2) at non-singleton dimension 3)

from user code:
   File "<string>", line 20, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''