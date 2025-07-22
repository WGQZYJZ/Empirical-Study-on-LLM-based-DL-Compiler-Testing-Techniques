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

    def __init__(self, min_value=-1.0, max_value=10):
        super().__init__()
        self.linear = torch.nn.Linear(64, 32)

    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = torch.clamp_min(v1, min_value)
        v3 = torch.clamp_max(v2, max_value)
        return v3


func = Model().to('cpu')


x1 = torch.randn(1000)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (1x1000 and 64x32)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., size=(1000,)), Parameter(FakeTensor(..., size=(32, 64), requires_grad=True)), Parameter(FakeTensor(..., size=(32,), requires_grad=True))), **{}):
a and b must have same reduction dim, but got [1, 1000] X [64, 32].

from user code:
   File "<string>", line 20, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/linear.py", line 125, in forward
    return F.linear(input, self.weight, self.bias)


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''