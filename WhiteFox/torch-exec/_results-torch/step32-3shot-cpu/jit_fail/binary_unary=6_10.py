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

    def __init__(self, other):
        super().__init__()
        self.linear = torch.nn.Linear(30, 784)
        self.other = other

    def forward(self, x1, x2):
        v1 = self.linear(x1)
        v2 = v1 - self.other
        v3 = torch.nn.ReLU()(v2)
        return v3


other = 0.5
func = Model(other).to('cpu')


num_hidden = 10
batch = 16
x1 = torch.randn(batch, num_hidden)

num_hidden = 10
batch = 16
x2 = torch.randn(batch, num_hidden)

test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (16x10 and 30x784)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., size=(16, 10)), Parameter(FakeTensor(..., size=(784, 30), requires_grad=True)), Parameter(FakeTensor(..., size=(784,), requires_grad=True))), **{}):
a and b must have same reduction dim, but got [16, 10] X [30, 784].

from user code:
   File "<string>", line 21, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/linear.py", line 125, in forward
    return F.linear(input, self.weight, self.bias)


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''