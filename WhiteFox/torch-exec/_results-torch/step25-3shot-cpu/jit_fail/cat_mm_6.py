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
        v1 = torch.mul(torch.t(x1), x2)
        v2 = torch.cat([v1, v1, v1, v1, v1, v1], 1)
        return v2



func = Model().to('cpu')


x1 = torch.rand((2, 4))

x2 = torch.rand((1, 3))

test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
The size of tensor a (2) must match the size of tensor b (3) at non-singleton dimension 1

jit:
Failed running call_function <built-in method mul of type object at 0x7bc76a196ec0>(*(FakeTensor(..., size=(s1, s0)), FakeTensor(..., size=(1, s2))), **{}):
The size of tensor a (s0) must match the size of tensor b (s2) at non-singleton dimension 1)

from user code:
   File "<string>", line 19, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''