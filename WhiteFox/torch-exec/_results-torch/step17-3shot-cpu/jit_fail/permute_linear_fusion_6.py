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
        self.linear = torch.nn.Linear(5, 10)
        self.linear2 = torch.nn.Linear(10, 5)

    def forward(self, x1):
        v1 = torch.matmul(x1, self.linear.weight)
        v2 = torch.matmul(v1, self.linear2.weight)
        return torch.relu(v2)



func = Model().to('cpu')


x1 = torch.randn(2, 5)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (2x5 and 10x5)

jit:
Failed running call_function <built-in method matmul of type object at 0x7b387b796ec0>(*(FakeTensor(..., size=(s0, s1)), Parameter(FakeTensor(..., size=(10, 5), requires_grad=True))), **{}):
a and b must have same reduction dim, but got [s0, s1] X [10, 5].

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''