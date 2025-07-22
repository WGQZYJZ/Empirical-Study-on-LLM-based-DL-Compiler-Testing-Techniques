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

    def __init__(self, min_value):
        super().__init__()
        self.conv = torch.nn.Conv2d(2, 10, 4)
        self.relu = torch.nn.ReLU()
        self.maxpool = torch.nn.MaxPool2d(3, stride=1, padding=1)
        self.flatten = torch.nn.Flatten()
        self.linear = torch.nn.Linear(1440, 500)
        self.tanh = torch.nn.Tanh()
        self.min_value = min_value

    def forward(self, x1, x2):
        v1 = self.conv(x1)
        v2 = torch.clamp_min(v1, self.min_value)
        v3 = self.relu(v2)
        v4 = self.maxpool(v3)
        v5 = self.conv(x2)
        v6 = torch.clamp_min(v5, self.min_value)
        v7 = self.relu(v6)
        v8 = self.maxpool(v7)
        v9 = self.flatten(v4)
        v10 = self.flatten(v8)
        v11 = torch.add(v9, v10)
        v12 = self.linear(v11)
        v13 = self.tanh(v12)
        return v13


min_value = -0.1

func = Model(min_value).to('cpu')


x1 = torch.randn(1, 2, 398, 398)

x2 = torch.randn(1, 2, 398, 398)

test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (1x1560250 and 1440x500)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., size=(1, 1560250)), Parameter(FakeTensor(..., size=(500, 1440), requires_grad=True)), Parameter(FakeTensor(..., size=(500,), requires_grad=True))), **{}):
a and b must have same reduction dim, but got [1, 1560250] X [1440, 500].

from user code:
   File "<string>", line 37, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/linear.py", line 125, in forward
    return F.linear(input, self.weight, self.bias)


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''