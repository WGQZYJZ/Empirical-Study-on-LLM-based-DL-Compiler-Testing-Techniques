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
        v1 = torch.matmul(x1, x2.transpose(-2, -1))
        v2 = v1.div(0.125)
        v3 = torch.nn.functional.softmax(v2, dim=-1)
        v4 = torch.nn.functional.dropout(v3, p=0.25)
        v5 = torch.matmul(v4, x3)
        return v5


func = Model().to('cpu')


x1 = torch.randn(2, 5)

x2 = torch.randn(5, 3)

x3 = torch.randn(3, 6)

test_inputs = [x1, x2, x3]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (2x5 and 3x5)

jit:
Failed running call_function <built-in method matmul of type object at 0x7b9ff6996ec0>(*(FakeTensor(..., size=(s2, s3)), FakeTensor(..., size=(s1, s0))), **{}):
a and b must have same reduction dim, but got [s2, s3] X [s1, s0].

from user code:
   File "<string>", line 19, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''