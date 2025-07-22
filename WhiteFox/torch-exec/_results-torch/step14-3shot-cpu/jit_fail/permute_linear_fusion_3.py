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

    def forward(self, x1):
        v5 = torch.randn_like(x1)
        v1 = torch.nn.functional.relu(x1.permute(0, 2, 1))
        v3 = x1.detach()
        v4 = torch.sum(v3, dim=-1, keepdim=True)
        v2 = x1.permute(0, 2, 1)
        v3 = torch.sum(v3)
        return torch.nn.functional.linear(v2, torch.where(v3 > 0, v4 * v5, v3), self.linear.bias)



func = Model().to('cpu')


x = torch.randn(1, 2, 2)

test_inputs = [x]

# JIT_FAIL
'''
direct:
t() expects a tensor with <= 2 dimensions, but self is 3D

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., size=(1, 2, 2)), FakeTensor(..., size=(1, 2, 2)), Parameter(FakeTensor(..., size=(2,), requires_grad=True))), **{}):
t() expects a tensor with <= 2 dimensions, but self is 3D

from user code:
   File "<string>", line 26, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''