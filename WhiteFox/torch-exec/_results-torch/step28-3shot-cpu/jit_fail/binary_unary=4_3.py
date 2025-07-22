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
        self.linear = torch.nn.Linear(1, 3)

    def forward(self, x1, x2, x3):
        x3 = 0.6 * x3
        x1 = 0.5 * x1
        l1 = self.linear(x1)
        l2 = self.linear(l1)
        v1 = torch.add(l2, x2, alpha=x3)
        v2 = torch.relu(v1)
        return v2


func = Model().to('cpu')


x1 = torch.randn(2, 1)

x2 = torch.randn(2, 3)
x3 = 1

test_inputs = [x1, x2, x3]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (2x3 and 1x3)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., size=(s0, 3)), Parameter(FakeTensor(..., size=(3, 1), requires_grad=True)), Parameter(FakeTensor(..., size=(3,), requires_grad=True))), **{}):
a and b must have same reduction dim, but got [s0, 3] X [1, 3].

from user code:
   File "<string>", line 23, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/linear.py", line 125, in forward
    return F.linear(input, self.weight, self.bias)


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''