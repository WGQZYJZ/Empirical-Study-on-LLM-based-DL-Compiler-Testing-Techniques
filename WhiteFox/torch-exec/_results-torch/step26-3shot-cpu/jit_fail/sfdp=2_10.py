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

    def forward(self, x1, x2, x3):
        k1 = torch.matmul(x1, x3.transpose(-2, -1))
        k2 = k1.div(0.30000001192092896)
        x4 = torch.nn.functional.softmax(k2, dim=-1)
        x5 = torch.nn.functional.dropout(x4, 0.2)
        x6 = torch.matmul(x5, x2)
        return x6


func = Model().to('cpu')


x1 = torch.randn(16, 5, 5)

x2 = torch.randn(16, 5, 10)

x3 = torch.randn(5, 10)

test_inputs = [x1, x2, x3]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (80x5 and 10x5)

jit:
Failed running call_function <built-in method matmul of type object at 0x7d6862d96ec0>(*(FakeTensor(..., size=(16, 5, 5)), FakeTensor(..., size=(10, 5))), **{}):
a and b must have same reduction dim, but got [80, 5] X [10, 5].

from user code:
   File "<string>", line 19, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''