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
        self.linear_q = torch.nn.Linear(64, 32)
        self.linear_k = torch.nn.Linear(64, 32)
        self.scale_factor = math.sqrt(32)

    def forward(self, x1, x2):
        v1 = self.linear_q(x1)
        v2 = self.linear_k(x2)
        v3 = torch.matmul(v1, v2)
        v4 = v3.mul(self.scale_factor)
        v5 = v4.softmax(dim=-1)
        v6 = torch.nn.functional.dropout(v5, p=0.5)
        v7 = torch.matmul(v6, x2)
        return v7


func = Model().to('cpu')


x1 = torch.randn(4, 64)

x2 = torch.randn(2, 64)

test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (4x32 and 2x32)

jit:
Failed running call_function <built-in method matmul of type object at 0x7bf95f996ec0>(*(FakeTensor(..., size=(4, 32)), FakeTensor(..., size=(2, 32))), **{}):
a and b must have same reduction dim, but got [4, 32] X [2, 32].

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''