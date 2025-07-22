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
        self.relu = torch.nn.ReLU()
        self.linear2 = torch.nn.Linear(2, 1)

    def forward(self, x1):
        v1 = x1.permute(0, 2, 1)
        v2 = torch.nn.functional.linear(v1, self.linear.weight, self.linear.bias)
        v4 = self.relu(v2)
        v3 = torch.max(v4, dim=-1)[0]
        v3 = v3.unsqueeze(dim=-1)
        v4 = v3 == -1
        v4 = torch.nn.functional.linear(v4, self.linear2.weight, self.linear2.bias)
        return v4



func = Model().to('cpu')


x1 = torch.randn(1, 2, 2)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 must have the same dtype, but got Bool and Float

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., size=(1, 2, 1), dtype=torch.bool), Parameter(FakeTensor(..., size=(1, 2), requires_grad=True)), Parameter(FakeTensor(..., size=(1,), requires_grad=True))), **{}):
a and b must have same reduction dim, but got [2, 1] X [2, 1].

from user code:
   File "<string>", line 28, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''