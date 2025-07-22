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

    def __init__(self, min_value: float=0.0, max_value: float=1.0):
        super().__init__()
        self.linear = torch.nn.Linear(5, 10)
        self.min_value = min_value
        self.max_value = max_value

    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = torch.clamp_min(v1, self.min_value)
        v3 = torch.clamp_max(v2, self.max_value)
        return v3


func = Model().to('cpu')


x1 = torch.randn(10, 5, 1)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (50x1 and 5x10)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., size=(s0, s1, 1)), Parameter(FakeTensor(..., size=(10, 5), requires_grad=True)), Parameter(FakeTensor(..., size=(10,), requires_grad=True))), **{}):
a and b must have same reduction dim, but got [s0*s1, 1] X [5, 10].

from user code:
   File "<string>", line 22, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/linear.py", line 125, in forward
    return F.linear(input, self.weight, self.bias)


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''