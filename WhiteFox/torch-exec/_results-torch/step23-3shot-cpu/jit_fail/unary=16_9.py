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
        self.linear = torch.nn.Linear(1024, 10)
        self.bn = torch.nn.BatchNorm2d(1024)

    def forward(self, x):
        v1 = self.linear(x)
        v2 = self.bn(v1)
        v3 = torch.relu(v2)
        return v3


func = Model().to('cpu')


x = torch.randn(1, 1024, 1, 1)

test_inputs = [x]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (1024x1 and 1024x10)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., size=(1, 1024, 1, 1)), Parameter(FakeTensor(..., size=(10, 1024), requires_grad=True)), Parameter(FakeTensor(..., size=(10,), requires_grad=True))), **{}):
a and b must have same reduction dim, but got [1024, 1] X [1024, 10].

from user code:
   File "<string>", line 21, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/linear.py", line 125, in forward
    return F.linear(input, self.weight, self.bias)


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''