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
        v1 = x1.permute(0, 2, 1)
        v2 = torch.nn.functional.linear(v1, self.linear.weight, self.linear.bias)
        x2 = torch.nn.functional.relu(v2)
        v3 = torch.nn.functional.tanh(x2)
        c1 = v3.view(1, -1)
        x2 = x2.permute(0, 2, 1)
        x3 = x2.permute(0, 2, 1)
        v3 = torch.matmul(x2, v3)
        x4 = v3.permute(0, 2, 1)
        v3 = torch.matmul(x4, x2)
        v3 = v3 + x2
        x1 = torch.sigmoid(v1)
        x4 = v3 + x4
        v3 = torch.mul(x2, x1)
        v3 = torch.sin(v2)
        c1 = c1 + v3
        c1 = c1 + v3
        return c1



func = Model().to('cpu')


x1 = torch.randn(1, 2, 2)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
The size of tensor a (4) must match the size of tensor b (2) at non-singleton dimension 2

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., size=(1, 4)), FakeTensor(..., size=(1, 2, 2))), **{}):
The size of tensor a (4) must match the size of tensor b (2) at non-singleton dimension 2)

from user code:
   File "<string>", line 35, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''