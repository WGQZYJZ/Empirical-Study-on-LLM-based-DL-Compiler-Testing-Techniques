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
        self.linear_1 = torch.nn.Linear(10, 10)
        self.linear_2 = torch.nn.Linear(10, 1)

    def forward(self, x1):
        v1 = self.linear_1(x1)
        v2 = self.linear_2(v1)
        return v2 + other


func = Model().to('cpu')


x1 = torch.randn(1, 10, 16, 17)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (160x17 and 10x10)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., size=(1, 10, 16, 17)), Parameter(FakeTensor(..., size=(10, 10), requires_grad=True)), Parameter(FakeTensor(..., size=(10,), requires_grad=True))), **{}):
a and b must have same reduction dim, but got [160, 17] X [10, 10].

from user code:
   File "<string>", line 21, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/linear.py", line 125, in forward
    return F.linear(input, self.weight, self.bias)


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''