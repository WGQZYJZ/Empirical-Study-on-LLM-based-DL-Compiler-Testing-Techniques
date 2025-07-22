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

    def __init__(self, negative_slope: float):
        super().__init__()
        self.negative_slope = negative_slope

    def forward(self, x1):
        v1 = torch.nn.functional.linear(x1, torch.ones_like(x1), bias=torch.zeros_like(x1))
        v2 = v1 > 0
        v3 = self.negative_slope * v1
        v4 = torch.where(v2, v1, v3)
        return v4


negative_slope = 1

func = Model(negative_slope).to('cpu')


x1 = torch.randn(2, 3, 4)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
t() expects a tensor with <= 2 dimensions, but self is 3D

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., size=(2, 3, 4)), FakeTensor(..., size=(2, 3, 4))), **{'bias': FakeTensor(..., size=(2, 3, 4))}):
t() expects a tensor with <= 2 dimensions, but self is 3D

from user code:
   File "<string>", line 20, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''