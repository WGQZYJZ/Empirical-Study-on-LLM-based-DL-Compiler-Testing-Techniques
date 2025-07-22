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
        self.upsample = torch.nn.Upsample(scale_factor=2, mode='nearest')
        self.linear_1 = torch.nn.Linear(5, 20)
        self.linear_2 = torch.nn.Linear(20, 10)

    def forward(self, x1):
        v1 = torch.relu(x1)
        v2 = torch.cat([x1, 2 * v1], 1)
        v3 = self.linear_1(v2)
        v4 = self.linear_2(v3)
        return v4



func = Model().to('cpu')


x1 = torch.randn(1, 5)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (1x10 and 5x20)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., size=(1, 2*s0)), Parameter(FakeTensor(..., size=(20, 5), requires_grad=True)), Parameter(FakeTensor(..., size=(20,), requires_grad=True))), **{}):
a and b must have same reduction dim, but got [1, 2*s0] X [5, 20].

from user code:
   File "<string>", line 24, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/linear.py", line 125, in forward
    return F.linear(input, self.weight, self.bias)


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''