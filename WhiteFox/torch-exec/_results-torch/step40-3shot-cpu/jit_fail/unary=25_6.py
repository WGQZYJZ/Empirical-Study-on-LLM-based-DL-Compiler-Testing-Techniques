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
        v1 = x1.shape[1]
        v2 = torch.empty([v1], dtype=torch.float32)
        i1 = 1
        while i1 < v1 + 1:
            v2[i1 - 1] = self.negative_slope * (self.negative_slope + 2) / 2
            i1 = i1 + 1
        v3 = v1 * torch.tensor(-0.5, dtype=torch.float32)
        v4 = v3 - v2
        i1 = 1
        while i1 < v1 + 1:
            v4[i1 - 1] = -(v3[i1 - 1] + v2[i1 - 1])
            i1 = i1 + 1
        v5 = torch.where(x1 > 0, x1, v4)
        return v5


negative_slope = 1

func = Model(negative_slope).to('cpu')



x1 = torch.randn(2, 4, dtype=torch.float32)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
invalid index of a 0-dim tensor. Use `tensor.item()` in Python or `tensor.item<T>()` in C++ to convert a 0-dim tensor to a number

jit:
Failed running call_function <built-in function getitem>(*(FakeTensor(..., size=()), 0), **{}):
invalid index of a 0-dim tensor. Use `tensor.item()` in Python or `tensor.item<T>()` in C++ to convert a 0-dim tensor to a number

from user code:
   File "<string>", line 30, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''