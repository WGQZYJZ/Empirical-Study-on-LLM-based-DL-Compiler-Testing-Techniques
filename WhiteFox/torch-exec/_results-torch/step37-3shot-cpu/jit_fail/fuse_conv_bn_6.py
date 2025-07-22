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
        self.conv1 = torch.nn.Conv2d(64, 64, kernel_size=3, padding=1, stride=2)
        self.conv2 = torch.nn.Conv2d(64, 32, kernel_size=1)
        self.conv3 = torch.nn.Conv2d(32, 20, kernel_size=3, padding=1)
        self.fc = torch.nn.Linear(20 * 8 * 8, 120)
        self.bn1 = torch.nn.BatchNorm2d(64)
        self.bn2 = torch.nn.BatchNorm2d(32)

    def forward(self, x):
        x1 = self.conv1(x)
        x2 = self.bn1(x1)
        x3 = self.conv2(x2)
        x4 = self.bn2(x3)
        x5 = self.conv3(x4)
        x6 = x5.view(x5.size(0), -1)
        x7 = self.fc(x6)
        return x7



func = Model().to('cpu')


x = torch.randn(1, 64, 8, 8)

test_inputs = [x]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (1x320 and 1280x120)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., size=(1, 320)), Parameter(FakeTensor(..., size=(120, 1280), requires_grad=True)), Parameter(FakeTensor(..., size=(120,), requires_grad=True))), **{}):
a and b must have same reduction dim, but got [1, 320] X [1280, 120].

from user code:
   File "<string>", line 31, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/linear.py", line 125, in forward
    return F.linear(input, self.weight, self.bias)


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''