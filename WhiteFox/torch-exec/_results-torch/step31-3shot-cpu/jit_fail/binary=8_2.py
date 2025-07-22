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
        self.conv = torch.nn.Conv2d(3, 4, 1, stride=1, padding=1)
        self.fc = torch.nn.Linear(4, 16)

    def forward(self, x1, x2):
        v1 = self.conv(x1)
        v2 = self.fc(x2)
        v3 = v1 + v2
        return v3


func = Model().to('cpu')


x1 = torch.randn(1, 3, 480, 640)

x2 = torch.randn(1, 4, 160, 1920)

test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (640x1920 and 4x16)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., size=(1, 4, 160, 1920)), Parameter(FakeTensor(..., size=(16, 4), requires_grad=True)), Parameter(FakeTensor(..., size=(16,), requires_grad=True))), **{}):
a and b must have same reduction dim, but got [640, 1920] X [4, 16].

from user code:
   File "<string>", line 22, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/linear.py", line 125, in forward
    return F.linear(input, self.weight, self.bias)


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''