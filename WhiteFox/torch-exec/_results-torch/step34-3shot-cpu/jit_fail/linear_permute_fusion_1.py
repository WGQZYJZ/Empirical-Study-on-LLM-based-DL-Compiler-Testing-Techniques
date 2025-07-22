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
        self.linear1 = torch.nn.Linear(2, 2)
        self.linear2 = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1 = torch.nn.functional.linear(x1, self.linear1.weight, self.linear1.bias)
        v2 = torch.nn.functional.linear(v1, self.linear2.weight, self.linear2.bias)
        t1 = v1.permute(0, 2, 1)
        v3 = torch.nn.functional.linear(t1, v1, self.linear1.bias)
        v4 = torch.tanh(v3)
        return v4



func = Model().to('cpu')


x1 = torch.randn(1, 2, 2)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
t() expects a tensor with <= 2 dimensions, but self is 3D

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., size=(1, 2, 2)), FakeTensor(..., size=(1, 2, 2)), Parameter(FakeTensor(..., size=(2,), requires_grad=True))), **{}):
t() expects a tensor with <= 2 dimensions, but self is 3D

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''