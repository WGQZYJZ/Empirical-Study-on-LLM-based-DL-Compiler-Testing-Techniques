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

class ModelTanh(torch.nn.Module):

    def __init__(self):
        super(ModelTanh, self).__init__()
        self.tanh = torch.nn.Tanh()
        self.flatten = torch.nn.Flatten(start_dim=2, end_dim=-1)
        self.linear_1 = torch.nn.Linear(8 * 8 * 5, 64)
        self.linear_2 = torch.nn.Linear(64, 64)
        self.linear_3 = torch.nn.Linear(64, 10, dtype=torch.float)

    def forward(self, x):
        x1 = x.to(torch.float)
        x2 = self.flatten(x1)
        x3 = self.linear_1(x2)
        x4 = self.tanh(x3)
        x5 = self.linear_2(x4)
        x6 = self.linear_3(x5)
        x6 = torch.tanh(x6)
        return x6



func = ModelTanh().to('cpu')


x = torch.randn(70, 8, 8, 5)

test_inputs = [x]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (560x40 and 320x64)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., size=(70, 8, 40)), Parameter(FakeTensor(..., size=(64, 320), requires_grad=True)), Parameter(FakeTensor(..., size=(64,), requires_grad=True))), **{}):
a and b must have same reduction dim, but got [560, 40] X [320, 64].

from user code:
   File "<string>", line 26, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/linear.py", line 125, in forward
    return F.linear(input, self.weight, self.bias)


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''