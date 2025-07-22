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
        v3 = torch.max(v2, dim=-1)[1]
        v4 = self.linear(v1)
        x = torch.tensor([[[1, 1], [1.2, 1], [3, 3]]])
        w1 = torch.nn.functional.softmax(x, dim=-1)
        w2 = torch.nn.functional.sigmoid(x)
        w3 = torch.nn.functional.softplus(x)
        z = w1 + w2 + w3
        return self.linear(z)



func = Model().to('cpu')


x1 = torch.randn(1, 3, 2)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (2x3 and 2x2)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., size=(1, 2, s0)), Parameter(FakeTensor(..., size=(2, 2), requires_grad=True)), Parameter(FakeTensor(..., size=(2,), requires_grad=True))), **{}):
a and b must have same reduction dim, but got [2, s0] X [2, 2].

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''