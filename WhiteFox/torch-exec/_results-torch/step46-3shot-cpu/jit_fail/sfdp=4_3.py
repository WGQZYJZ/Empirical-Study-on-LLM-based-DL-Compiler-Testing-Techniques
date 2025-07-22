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

class Module1(torch.nn.Module):

    def __init__(self):
        super().__init__()

    def forward(self, x):
        x = x + x
        x = x + x
        return x

class Module0(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(4, 4, 1)
        self.conv2 = Module1()

    def forward(self, x):
        x = self.conv1(x)
        x = self.conv2(x)
        return x

class model(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(18, 36)
        self.linear2 = torch.nn.Linear(36, 72)

    def forward(self, x):
        x = self.linear1(x)
        x = self.linear2(x)
        return x



func = model().to('cpu')


x = torch.randn(1, 4, 12, 12)

test_inputs = [x]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (48x12 and 18x36)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., size=(1, 4, 12, 12)), Parameter(FakeTensor(..., size=(36, 18), requires_grad=True)), Parameter(FakeTensor(..., size=(36,), requires_grad=True))), **{}):
a and b must have same reduction dim, but got [48, 12] X [18, 36].

from user code:
   File "<string>", line 43, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/linear.py", line 125, in forward
    return F.linear(input, self.weight, self.bias)


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''