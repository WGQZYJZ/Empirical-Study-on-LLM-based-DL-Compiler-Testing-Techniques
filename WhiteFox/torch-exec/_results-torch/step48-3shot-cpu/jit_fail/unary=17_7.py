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
        self.conv_transpose = torch.nn.ConvTranspose2d(3, 32, kernel_size=3, stride=3)
        self.pool = torch.nn.AvgPool2d(3, stride=3)
        self.fc1 = torch.nn.Linear(3264, 256)
        self.fc2 = torch.nn.Linear(256, 128)
        self.fc3 = torch.nn.Linear(128, 3)

    def forward(self, x1):
        v1 = self.conv_transpose(x1)
        v2 = self.pool(v1)
        v3 = torch.flatten(v2, 1)
        v4 = self.fc1(v3)
        v5 = torch.relu(v4)
        v6 = self.fc2(v5)
        v7 = torch.relu(v6)
        v8 = self.fc3(v7)
        return v8



func = Model().to('cpu')


x1 = torch.randn(1, 3, 240, 320)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (1x2457600 and 3264x256)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., size=(1, 2457600)), Parameter(FakeTensor(..., size=(256, 3264), requires_grad=True)), Parameter(FakeTensor(..., size=(256,), requires_grad=True))), **{}):
a and b must have same reduction dim, but got [1, 2457600] X [3264, 256].

from user code:
   File "<string>", line 27, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/linear.py", line 125, in forward
    return F.linear(input, self.weight, self.bias)


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''