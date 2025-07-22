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
        self.bias1 = torch.nn.Parameter(torch.Tensor(1))
        self.bias2 = torch.nn.Parameter(torch.Tensor(1))

    def forward(self, input1):
        v1 = torch.nn.functional.linear(input1, torch.ones(256), self.bias1)
        v2 = v1.clamp(min=0, max=6)
        v3 = v2 + 3
        v4 = v3 * 6
        return v4


func = Model().to('cpu')


__input__ = torch.randn(1, 256)

test_inputs = [__input__]

# JIT_FAIL
'''
direct:
mat2 must be a matrix, got 1-D tensor

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., size=(1, 256)), FakeTensor(..., size=(256,)), Parameter(FakeTensor(..., size=(1,), requires_grad=True))), **{}):
b must be 2D

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''