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
        v1 = torch.nn.functional.interpolate(x1, scale_factor=[2, 1])
        return v1



func = Model().to('cpu')


x1 = torch.randn(10, 7, 5)
x2 = 1

test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
Input and scale_factor must have the same number of spatial dimensions, but got input with spatial dimensions of [5] and scale_factor of shape [2, 1]. Please provide input tensor in (N, C, d1, d2, ...,dK) format and scale_factor in (s1, s2, ...,sK) format.

jit:
Failed running call_function <function interpolate at 0x7dea305850d0>(*(FakeTensor(..., size=(s0, s1, s2)),), **{'scale_factor': [2, 1]}):
Input and scale_factor must have the same number of spatial dimensions, but got input with spatial dimensions of [s2] and scale_factor of shape [2, 1]. Please provide input tensor in (N, C, d1, d2, ...,dK) format and scale_factor in (s1, s2, ...,sK) format.

from user code:
   File "<string>", line 19, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''