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
        self.conv1 = torch.nn.Conv2d(in_channels=3, out_channels=8, kernel_size=1, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(in_channels=8, out_channels=16, kernel_size=1, stride=1, padding=1)
        self.conv3 = torch.nn.Conv2d(in_channels=16, out_channels=48, kernel_size=1, stride=1, padding=1)
        self.conv4 = torch.nn.Conv2d(in_channels=48, out_channels=96, kernel_size=1, stride=1, padding=1)
        self.flatten = torch.nn.Flatten()
        self.fc = torch.nn.Linear(in_features=16 * 6 * 6, out_features=16)

    def forward(self, x):
        v1 = self.conv1(x)
        v2 = self.flatten(v1)
        v3 = self.fc(v2)
        v4 = torch.sigmoid(v3)
        return v4



func = Model().to('cpu')


x = torch.randn(1, 3, 64, 64)

test_inputs = [x]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (1x34848 and 576x16)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., size=(1, 34848)), Parameter(FakeTensor(..., size=(16, 576), requires_grad=True)), Parameter(FakeTensor(..., size=(16,), requires_grad=True))), **{}):
a and b must have same reduction dim, but got [1, 34848] X [576, 16].

from user code:
   File "<string>", line 27, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/linear.py", line 125, in forward
    return F.linear(input, self.weight, self.bias)


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''