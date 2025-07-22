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
        v1 = x1 @ torch.ones([256, 2560])
        v2 = v1 + 3
        v3 = torch.clamp_min(v2, 0)
        v4 = torch.clamp_max(v3, 6)
        v5 = v4 / 6
        return v5


func = Model().to('cpu')


x1 = torch.randn(1, 10000)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (1x10000 and 256x2560)

jit:
Failed running call_function <built-in function matmul>(*(FakeTensor(..., size=(1, 10000)), FakeTensor(..., size=(256, 2560))), **{}):
a and b must have same reduction dim, but got [1, 10000] X [256, 2560].

from user code:
   File "<string>", line 19, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''