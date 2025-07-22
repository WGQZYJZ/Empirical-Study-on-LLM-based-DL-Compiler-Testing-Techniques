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

class Layer(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.conv2d = torch.nn.Conv2d(1, 1, (1, 1))
        self.flatten1 = torch.nn.Flatten()
        self.linear1 = torch.nn.Linear(8, 6)
        self.linear2 = torch.nn.Linear(6, 4, bias=False)
        self.relu1 = torch.nn.ReLU()
        self.flatten2 = torch.nn.Flatten()
        self.linear3 = torch.nn.Linear(8, 8)

    def forward(self, x1):
        v1 = self.conv2d(x1)
        v2 = self.flatten1(v1)
        v3 = self.linear1(v1)
        v4 = self.relu1(v2)
        v5 = self.linear2(v3)
        v6 = self.relu1(v4)
        v7 = torch.matmul(v5, v6)
        v8 = self.flatten2(v6)
        v9 = self.linear3(v8)
        return v7 + v8 + v9



func = Layer().to('cpu')


x1 = torch.randn(1, 1, 6, 6)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (6x6 and 8x6)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., size=(1, 1, 6, 6)), Parameter(FakeTensor(..., size=(6, 8), requires_grad=True)), Parameter(FakeTensor(..., size=(6,), requires_grad=True))), **{}):
a and b must have same reduction dim, but got [6, 6] X [8, 6].

from user code:
   File "<string>", line 28, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/linear.py", line 125, in forward
    return F.linear(input, self.weight, self.bias)


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''