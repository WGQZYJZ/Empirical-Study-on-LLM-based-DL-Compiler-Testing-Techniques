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
        self.linear = torch.nn.Linear(3, 3)
        self.act = torch.nn.modules.activation.Sigmoid()

    def forward(self, x1):
        v1 = torch.nn.functional.linear(x1, self.linear.weight, self.linear.bias)
        v2 = self.act(v1)
        v3 = v2.permute(1, 0)
        v5 = v3.clone().detach()
        v4 = v3.permute(1, 0)
        v7 = v5.add(v4)
        return v7 + v2



func = Model().to('cpu')


x1 = torch.randn(3, 2)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (3x2 and 3x3)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., size=(s0, s1)), Parameter(FakeTensor(..., size=(3, 3), requires_grad=True)), Parameter(FakeTensor(..., size=(3,), requires_grad=True))), **{}):
a and b must have same reduction dim, but got [s0, s1] X [3, 3].

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''