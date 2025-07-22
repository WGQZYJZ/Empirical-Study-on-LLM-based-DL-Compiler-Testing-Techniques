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

    def __init__(self, i):
        super().__init__()
        self.linear = torch.nn.Linear(i, 1)

    def forward(self, x2, x3, x4):
        v0 = torch.add(x3, x4)
        v1 = self.linear(x2)
        v8 = torch.add(v1, v0)
        return v8


i = 1

func = Model(i).to('cpu')


x2 = torch.randn(1, 100)

x3 = torch.randn(1, 100)

x4 = torch.randn(1, 100)

test_inputs = [x2, x3, x4]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (1x100 and 1x1)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., size=(1, 100)), Parameter(FakeTensor(..., size=(1, 1), requires_grad=True)), Parameter(FakeTensor(..., size=(1,), requires_grad=True))), **{}):
a and b must have same reduction dim, but got [1, 100] X [1, 1].

from user code:
   File "<string>", line 21, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/linear.py", line 125, in forward
    return F.linear(input, self.weight, self.bias)


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''