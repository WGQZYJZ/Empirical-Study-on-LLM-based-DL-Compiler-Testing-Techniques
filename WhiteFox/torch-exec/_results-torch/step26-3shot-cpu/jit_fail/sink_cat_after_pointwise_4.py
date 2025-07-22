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
        self.m1 = torch.nn.Linear(1, 2)
        self.m2 = torch.nn.Linear(10, 10)

    def forward(self, x):
        x = torch.cat([x, x], dim=1)
        x = torch.relu(x + self.m1(x))
        return self.m2(x)



func = Model().to('cpu')


x = torch.randn(3, 2, 2)

test_inputs = [x]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (12x2 and 1x2)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., size=(3, 4, 2)), Parameter(FakeTensor(..., size=(2, 1), requires_grad=True)), Parameter(FakeTensor(..., size=(2,), requires_grad=True))), **{}):
a and b must have same reduction dim, but got [12, 2] X [1, 2].

from user code:
   File "<string>", line 22, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/linear.py", line 125, in forward
    return F.linear(input, self.weight, self.bias)


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''