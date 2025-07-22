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
        self.linear = torch.nn.Linear(24, 32)

    def forward(self, x1, x2):
        v1 = torch.sqrt(x2)
        v2 = self.linear(x2)
        v3 = v1 + v2 - x1
        return v3


func = Model().to('cpu')


x1 = torch.randn(1, 3, 64, 64)

x2 = torch.randn(1, 3)

test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (1x3 and 24x32)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., size=(1, s0)), Parameter(FakeTensor(..., size=(32, 24), requires_grad=True)), Parameter(FakeTensor(..., size=(32,), requires_grad=True))), **{}):
a and b must have same reduction dim, but got [1, s0] X [24, 32].

from user code:
   File "<string>", line 21, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/linear.py", line 125, in forward
    return F.linear(input, self.weight, self.bias)


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''