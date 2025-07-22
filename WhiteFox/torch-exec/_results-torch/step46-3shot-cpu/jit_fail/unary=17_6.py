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
        stride = 2
        stride2 = 16
        stride3 = stride2 * stride
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose2d(3, 32, 3, stride=stride)
        self.relu1 = torch.nn.ReLU(inplace=True)
        self.fc = torch.nn.Linear(int(32 * stride2 * stride2 / 16 * stride3), 2)
        self.maxpool = torch.nn.MaxPool2d(3, stride=stride)

    def forward(self, x):
        v1 = self.conv_transpose(x)
        v2 = self.relu1(v1)
        v3 = v2.view(-1)
        v4 = self.fc(v3)
        v5 = v4.view(1, -1)
        v6 = self.maxpool(v5)
        return v6



func = Model().to('cpu')


x = torch.randn(1, 3, 24, 24)

test_inputs = [x]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (1x76832 and 16384x2)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., size=(76832,)), Parameter(FakeTensor(..., size=(2, 16384), requires_grad=True)), Parameter(FakeTensor(..., size=(2,), requires_grad=True))), **{}):
a and b must have same reduction dim, but got [1, 76832] X [16384, 2].

from user code:
   File "<string>", line 29, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/linear.py", line 125, in forward
    return F.linear(input, self.weight, self.bias)


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''