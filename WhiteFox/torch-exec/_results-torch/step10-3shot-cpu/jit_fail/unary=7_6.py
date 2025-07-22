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
        self.linear = torch.nn.Linear(952, 336)

    def forward(self, x1):
        v1 = x1.flatten(1, -1)
        v2 = self.linear(v1)
        v3 = torch.clamp(v2, max=6) + 3
        v4 = v3 * 0.16666666666666666
        return v4


func = Model().to('cpu')


x1 = torch.randn(1, 96, 88)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (1x8448 and 952x336)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., size=(1, s0*s1)), Parameter(FakeTensor(..., size=(336, 952), requires_grad=True)), Parameter(FakeTensor(..., size=(336,), requires_grad=True))), **{}):
a and b must have same reduction dim, but got [1, s0*s1] X [952, 336].

from user code:
   File "<string>", line 21, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/linear.py", line 125, in forward
    return F.linear(input, self.weight, self.bias)


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''