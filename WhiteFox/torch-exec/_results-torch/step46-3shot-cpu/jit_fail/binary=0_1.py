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
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(8, 16, 1, stride=1, padding=1)
        self.fc = torch.nn.Linear(8, 1)

    def conv_block(self, x1):
        v1 = self.conv1(x1)
        v2 = self.conv2(v1)
        v3 = self.fc(v2)
        return v3

    def forward(self, x1, x2):
        v1 = self.conv_block(x1)
        v2 = self.conv_block(x2)
        v3 = v1 * v2
        v4 = v3 + v2
        return v4



func = Model().to('cpu')


x1 = torch.randn(1, 3, 64, 64)

x2 = torch.randn(1, 3, 64, 64)

test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (1088x68 and 8x1)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., size=(1, 16, 68, 68)), Parameter(FakeTensor(..., size=(1, 8), requires_grad=True)), Parameter(FakeTensor(..., size=(1,), requires_grad=True))), **{}):
a and b must have same reduction dim, but got [1088, 68] X [8, 1].

from user code:
   File "<string>", line 28, in forward
  File "<string>", line 24, in conv_block
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/linear.py", line 125, in forward
    return F.linear(input, self.weight, self.bias)


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''