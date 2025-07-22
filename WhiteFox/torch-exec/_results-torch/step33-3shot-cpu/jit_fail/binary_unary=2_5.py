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
        self.conv1 = torch.nn.Conv2d(3, 20, 3, stride=1, padding=1)
        self.pool1 = torch.nn.MaxPool2d(kernel_size=2, stride=2, padding=0, dilation=1, ceil_mode=False)
        self.conv2 = torch.nn.Conv2d(20, 50, 3, stride=1, padding=1)
        self.pool2 = torch.nn.MaxPool2d(kernel_size=2, stride=2, padding=0, dilation=1, ceil_mode=False)
        self.fc1 = torch.nn.Linear(800, 500)
        self.relu = torch.nn.ReLU()
        self.fc2 = torch.nn.Linear(500, 10)

    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = self.pool1(v1)
        v3 = self.conv2(v2)
        v4 = self.pool2(v3)
        v5 = v4.view(v4.size(0), -1)
        v6 = self.fc1(v5)
        v7 = self.relu(v6)
        v8 = self.fc2(v7)
        return v8



func = Model().to('cpu')


x1 = torch.randn(1, 3, 64, 64)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (1x12800 and 800x500)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., size=(1, 12800)), Parameter(FakeTensor(..., size=(500, 800), requires_grad=True)), Parameter(FakeTensor(..., size=(500,), requires_grad=True))), **{}):
a and b must have same reduction dim, but got [1, 12800] X [800, 500].

from user code:
   File "<string>", line 31, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/linear.py", line 125, in forward
    return F.linear(input, self.weight, self.bias)


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''