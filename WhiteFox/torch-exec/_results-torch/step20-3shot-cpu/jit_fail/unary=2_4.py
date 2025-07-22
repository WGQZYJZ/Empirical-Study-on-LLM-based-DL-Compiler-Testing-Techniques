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
        self.conv_transpose = torch.nn.ConvTranspose1d(16, 16, kernel_size=1, stride=1, bias=True)

    def forward(self, x1):
        v1 = self.conv_transpose(x1)
        v2 = torch.nn.Softmax(dim=0)(torch.cat((v1, v1)))
        v3 = v2.max()[0]
        v4 = v2.min()[0]
        v5 = v3 + v4
        v6 = v5 * v4
        v7 = v6 * v5
        return v7



func = Model().to('cpu')


x1 = torch.randn(10, 16, 100)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
invalid index of a 0-dim tensor. Use `tensor.item()` in Python or `tensor.item<T>()` in C++ to convert a 0-dim tensor to a number

jit:
Failed running call_function <built-in function getitem>(*(FakeTensor(..., size=()), 0), **{}):
invalid index of a 0-dim tensor. Use `tensor.item()` in Python or `tensor.item<T>()` in C++ to convert a 0-dim tensor to a number

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''