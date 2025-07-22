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
        self.fc = torch.nn.Linear(64, 64)

    def forward(self, x1, _max_value=-1, _min_value=-1):
        max_value = _max_value
        min_value = _min_value
        v0 = x1.flatten(1)
        v1 = self.fc(v0)
        v2 = v1.clamp_min(min_value)
        v3 = v2.clamp_max(max_value)
        return v3


func = Model().to('cpu')


x1 = torch.randn(1, 64, 64)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (1x4096 and 64x64)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., size=(1, s0*s1)), Parameter(FakeTensor(..., size=(64, 64), requires_grad=True)), Parameter(FakeTensor(..., size=(64,), requires_grad=True))), **{}):
a and b must have same reduction dim, but got [1, s0*s1] X [64, 64].

from user code:
   File "<string>", line 23, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/linear.py", line 125, in forward
    return F.linear(input, self.weight, self.bias)


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''