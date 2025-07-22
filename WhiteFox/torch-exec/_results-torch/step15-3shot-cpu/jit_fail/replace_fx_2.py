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

    def forward(self, x1):
        c1 = torch.nn.functional.dropout(x1, p=0.3)
        c2 = torch.nn.functional.dropout(x1, p=0.5)
        c3 = torch.nn.Parameter(torch.rand(5, 4))
        c4 = torch.cat([c1, c2, c3], dim=2)
        c5 = torch.rand(4, 5)
        c6 = torch.nn.functional.linear(c5, c4)
        return c6



func = Model().to('cpu')


x1 = torch.randn(1, 2)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Dimension out of range (expected to be in range of [-2, 1], but got 2)

jit:
Failed running call_function <built-in method cat of type object at 0x716e9d996ec0>(*([FakeTensor(..., size=(1, s0)), FakeTensor(..., size=(1, s0)), FakeTensor(..., size=(5, 4), grad_fn=<TracableCreateParameterBackward>)],), **{'dim': 2}):
Dimension out of range (expected to be in range of [-2, 1], but got 2)

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''