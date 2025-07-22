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
        self.linear = torch.nn.Linear(4, 8)

    def forward(self, x1):
        v1 = self.linear(torch.relu(x1))
        v2 = v1 * 0.5
        v3 = v1 * 0.7071067811865476
        v4 = torch.erf(v3)
        v5 = v4 + 1
        v6 = v2 * v5
        return v6


func = Model().to('cpu')


x1 = torch.randn(1, 4, 1, 1)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (4x1 and 4x8)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., size=(1, s0, 1, 1)), Parameter(FakeTensor(..., size=(8, 4), requires_grad=True)), Parameter(FakeTensor(..., size=(8,), requires_grad=True))), **{}):
a and b must have same reduction dim, but got [s0, 1] X [4, 8].

from user code:
   File "<string>", line 20, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/linear.py", line 125, in forward
    return F.linear(input, self.weight, self.bias)


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''