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
        self.conv = torch.nn.Conv2d(16, 16, 7, stride=1, padding=3)
        self.fc = torch.nn.Linear(7, 7)

    def forward(self, x1):
        m1 = self.conv(x1)
        m2 = torch.relu(m1)
        m3 = m2.permute((0, 2, 3, 1))
        m4 = self.fc(m3)
        return m4



func = Model().to('cpu')


x1 = torch.randn(1, 16, 64, 64)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (4096x16 and 7x7)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., size=(1, 64, 64, 16)), Parameter(FakeTensor(..., size=(7, 7), requires_grad=True)), Parameter(FakeTensor(..., size=(7,), requires_grad=True))), **{}):
a and b must have same reduction dim, but got [4096, 16] X [7, 7].

from user code:
   File "<string>", line 24, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/linear.py", line 125, in forward
    return F.linear(input, self.weight, self.bias)


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''