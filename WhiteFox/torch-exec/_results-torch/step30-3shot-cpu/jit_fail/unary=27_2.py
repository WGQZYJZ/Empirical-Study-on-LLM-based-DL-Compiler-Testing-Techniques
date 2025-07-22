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

    def __init__(self, min, max, hidden):
        super().__init__()
        self.conv = torch.nn.Conv2d(8, 5, 1, stride=2, padding=1)
        self.min = min
        self.max = max
        self.model1 = torch.nn.Sequential(torch.nn.Linear(5, hidden), torch.nn.ReLU(), torch.nn.Linear(hidden, 2), torch.nn.ReLU())
        self.model2 = torch.nn.Sequential(torch.nn.Linear(2, hidden), torch.nn.ReLU(), torch.nn.Linear(hidden, 5), torch.nn.ReLU())

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.clamp_min(v1, self.min)
        v3 = torch.clamp_max(v2, self.max)
        v4 = self.model1(v3)
        v5 = self.model2(v4)
        return v5


min = 0.6
max = 0.8
hidden = 120

func = Model(min, max, hidden).to('cpu')


x1 = torch.randn(1, 8, 200, 250)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (505x126 and 5x120)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., size=(1, 5, 101, 126)), Parameter(FakeTensor(..., size=(120, 5), requires_grad=True)), Parameter(FakeTensor(..., size=(120,), requires_grad=True))), **{}):
a and b must have same reduction dim, but got [505, 126] X [5, 120].

from user code:
   File "<string>", line 27, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/container.py", line 250, in forward
    input = module(input)
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/linear.py", line 125, in forward
    return F.linear(input, self.weight, self.bias)


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''