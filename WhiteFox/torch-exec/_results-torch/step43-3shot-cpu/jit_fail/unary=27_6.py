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

    def __init__(self, min, max):
        super().__init__()
        self.conv = torch.nn.Conv2d(1, 2, 9, stride=4, padding=1)
        self.fc = torch.nn.Linear(20, 40)
        self.min = min
        self.max = max

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1.reshape(v1.size(0), -1)
        v3 = self.fc(v2)
        v4 = torch.clamp_min(v3, self.min)
        v5 = torch.clamp_max(v4, self.max)
        return v5


min = 3.0
max = 4.0

func = Model(min, max).to('cpu')


x1 = torch.randn(1, 1, 10, 10)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (1x2 and 20x40)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., size=(1, 2)), Parameter(FakeTensor(..., size=(40, 20), requires_grad=True)), Parameter(FakeTensor(..., size=(40,), requires_grad=True))), **{}):
a and b must have same reduction dim, but got [1, 2] X [20, 40].

from user code:
   File "<string>", line 25, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/linear.py", line 125, in forward
    return F.linear(input, self.weight, self.bias)


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''