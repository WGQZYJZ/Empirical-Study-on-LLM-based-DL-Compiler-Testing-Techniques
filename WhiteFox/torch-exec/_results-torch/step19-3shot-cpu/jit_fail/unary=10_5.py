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
        self.lr = torch.nn.Linear(16, 16, bias=False)

    def forward(self, x1):
        v1 = self.lr(x1)
        v2 = v1 + 3
        v3 = x1.clamp_min(0)
        v4 = x1.clamp_max(6)
        v5 = v4 / 6
        return v5


func = Model().to('cpu')


x1 = torch.randn(1, 16, 28, 28)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (448x28 and 16x16)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., size=(1, s0, s1, s2)), Parameter(FakeTensor(..., size=(16, 16), requires_grad=True)), None), **{}):
a and b must have same reduction dim, but got [s0*s1, s2] X [16, 16].

from user code:
   File "<string>", line 20, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/linear.py", line 125, in forward
    return F.linear(input, self.weight, self.bias)


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''