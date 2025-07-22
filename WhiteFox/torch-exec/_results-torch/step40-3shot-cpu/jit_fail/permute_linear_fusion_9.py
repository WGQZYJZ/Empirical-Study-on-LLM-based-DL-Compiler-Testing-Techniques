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
        self.linear = torch.nn.Linear(2, 2)
        self.linear2 = torch.nn.Linear(2, 1)
        self.linear3 = torch.nn.Linear(1, 2)

    def forward(self, x1):
        v1 = x1.permute(0, 2, 1)
        v2 = torch.nn.functional.linear(v1, self.linear.weight, self.linear.bias)
        x2 = torch.nn.functional.relu(v2)
        v3 = x2.permute(0, 2, 1)
        v4 = torch.nn.functional.linear(v3, self.linear2.weight, self.linear2.bias)
        v5 = torch.nn.functional.relu(v4)
        v6 = v5.permute(0, 2, 1)
        v7 = torch.nn.functional.linear(v6, self.linear3.weight, self.linear3.bias)
        v8 = torch.nn.functional.softmax(v7, dim=-1)
        return v8



func = Model().to('cpu')


x1 = torch.randn(1, 2, 2)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (1x2 and 1x2)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., size=(1, 1, 2)), Parameter(FakeTensor(..., size=(2, 1), requires_grad=True)), Parameter(FakeTensor(..., size=(2,), requires_grad=True))), **{}):
a and b must have same reduction dim, but got [1, 2] X [1, 2].

from user code:
   File "<string>", line 29, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''