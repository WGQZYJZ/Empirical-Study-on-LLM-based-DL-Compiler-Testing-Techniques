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
        v1 = torch.cat([v1, v1, v1, v1, v1], 0)
        v2 = torch.cat([v1, v1, v1, v1, v1], 1)
        v3 = torch.cat([v1, v1, v1, v1, v1], 2)
        v4 = torch.mm(v1, x2)
        v4 = torch.cat([v1, v1, v1, v1, v1], 0)
        return torch.cat([v4, v3, v2, v1, v4, v3, v2, v1], 0)



func = Model().to('cpu')


x1 = torch.randn(1, 1)

x2 = torch.randn(1, 3)

test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
Dimension out of range (expected to be in range of [-2, 1], but got 2)

jit:
Failed running call_function <built-in method cat of type object at 0x7a2290596ec0>(*([FakeTensor(..., size=(5, s0)), FakeTensor(..., size=(5, s0)), FakeTensor(..., size=(5, s0)), FakeTensor(..., size=(5, s0)), FakeTensor(..., size=(5, s0))], 2), **{}):
Dimension out of range (expected to be in range of [-2, 1], but got 2)

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''