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

    def __init__(self, negative_slope):
        super().__init__()
        self.linear = torch.nn.Linear(1, 8)

    def forward(self, x1, _negative_slope):
        v1 = self.linear(x1)
        v2 = v1 > 0
        v3 = -_negative_slope * v1
        v4 = torch.where(v2, v1, v3)
        return v4


negative_slope = 0.1
func = Model(negative_slope).to('cpu')


x1 = torch.randn(2, 1, 8)
_negative_slope = 1

test_inputs = [x1, _negative_slope]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (2x8 and 1x8)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., size=(s0, 1, s1)), Parameter(FakeTensor(..., size=(8, 1), requires_grad=True)), Parameter(FakeTensor(..., size=(8,), requires_grad=True))), **{}):
a and b must have same reduction dim, but got [s0, s1] X [1, 8].

from user code:
   File "<string>", line 20, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/linear.py", line 125, in forward
    return F.linear(input, self.weight, self.bias)


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''