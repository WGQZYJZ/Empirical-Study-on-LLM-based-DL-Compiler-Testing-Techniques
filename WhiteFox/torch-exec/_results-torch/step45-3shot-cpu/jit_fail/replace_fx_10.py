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
        for i in range(10):
            x1 += 1
        x2 = torch.randn(1, 2, 3)
        x3 = torch.rand_like(x1)
        x4 = x3 * torch.rand(1)
        x5 = x2 * x4
        return x5

class Model(torch.nn.Module):

    def __init__(self):
        super().__init__()

    def forward(self, x1):
        for i in range(10):
            x1 += 1
        x2 = torch.randn(1, 2, 3)
        x3 = torch.rand_like(x1)
        x4 = x3 * torch.rand(1)
        x5 = x2 * x4
        for j in range(10):
            x1 += 1
        return x5



func = Model().to('cpu')


x1 = torch.randn(1, 2, 2)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
The size of tensor a (3) must match the size of tensor b (2) at non-singleton dimension 2

jit:
Failed running call_function <built-in function mul>(*(FakeTensor(..., size=(1, 2, 3)), FakeTensor(..., size=(1, 2, 2))), **{}):
Attempting to broadcast a dimension of length 2 at -1! Mismatching argument at index 1 had torch.Size([1, 2, 2]); but expected shape should be broadcastable to [1, 2, 3]

from user code:
   File "<string>", line 38, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''