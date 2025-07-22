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

    def __init__(self, out_channel):
        super(Model, self).__init__()
        self.out_channel = out_channel
        self.linear = torch.nn.Linear(10, out_channel)

    def forward(self, x1, x2):
        t1 = self.linear(x)
        t2 = t1 + x2
        t3 = torch.nn.functional.relu(t2)
        return t3


out_channel = 1
func = Model(8).to('cpu')


x1 = torch.randn(5, 10)

x2 = torch.randn(5, 8)

test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (8x16 and 10x8)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., size=(8, 16)), Parameter(FakeTensor(..., size=(8, 10), requires_grad=True)), Parameter(FakeTensor(..., size=(8,), requires_grad=True))), **{}):
a and b must have same reduction dim, but got [8, 16] X [10, 8].

from user code:
   File "<string>", line 21, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/linear.py", line 125, in forward
    return F.linear(input, self.weight, self.bias)


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''