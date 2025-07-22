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
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.relu = torch.nn.functional.relu
        self.linear = torch.nn.Linear(100, 2)

    def forward(self, x1):
        v1 = torch.relu(self.conv(x1))
        v2 = torch.mean(v1, dim=(1, 2, 3))
        v3 = self.relu(self.linear(v1))
        return v3



func = Model().to('cpu')


x1 = torch.randn(16, 3, 256, 256)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (33024x258 and 100x2)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., size=(16, 8, 258, 258)), Parameter(FakeTensor(..., size=(2, 100), requires_grad=True)), Parameter(FakeTensor(..., size=(2,), requires_grad=True))), **{}):
a and b must have same reduction dim, but got [33024, 258] X [100, 2].

from user code:
   File "<string>", line 24, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/linear.py", line 125, in forward
    return F.linear(input, self.weight, self.bias)


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''