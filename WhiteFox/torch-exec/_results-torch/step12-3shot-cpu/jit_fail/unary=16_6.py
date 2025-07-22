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

    def __init__(self, in_channels=3, num_classes=10):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.linear = torch.nn.Linear(9216 * 4, 128)
        self.relu = torch.nn.ReLU()

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1.reshape((v1.shape[0], -1))
        v3 = self.linear(v2)
        v4 = self.relu(v3)
        return v4


func = Model().to('cpu')


x1 = torch.randn(1, 3, 64, 64)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (1x34848 and 36864x128)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., size=(1, 34848)), Parameter(FakeTensor(..., size=(128, 36864), requires_grad=True)), Parameter(FakeTensor(..., size=(128,), requires_grad=True))), **{}):
a and b must have same reduction dim, but got [1, 34848] X [36864, 128].

from user code:
   File "<string>", line 24, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/linear.py", line 125, in forward
    return F.linear(input, self.weight, self.bias)


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''