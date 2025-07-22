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

    def __init__(self, min_value=0.5, max_value=0.8):
        super().__init__()
        self.linear = torch.nn.Linear(6, 4)
        self.min_value = min_value
        self.max_value = max_value

    def forward(self, x1):
        (b, c, _, _) = x1.shape
        x1 = x1.reshape(b, -1)
        v1 = self.linear(x1)
        v2 = v1.clamp(min=self.min_value)
        v3 = v2.clamp(max=self.max_value)
        return v3


func = Model(min_value=min_value, max_value=max_value).to('cpu')


x1 = torch.randn(1, 6, 10, 8)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (1x480 and 6x4)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., size=(1, s0*s1*s2)), Parameter(FakeTensor(..., size=(4, 6), requires_grad=True)), Parameter(FakeTensor(..., size=(4,), requires_grad=True))), **{}):
a and b must have same reduction dim, but got [1, s0*s1*s2] X [6, 4].

from user code:
   File "<string>", line 24, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/linear.py", line 125, in forward
    return F.linear(input, self.weight, self.bias)


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''