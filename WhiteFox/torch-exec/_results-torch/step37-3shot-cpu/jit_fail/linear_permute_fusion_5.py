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
        self.linear = torch.nn.Linear(1, 16)
        self.relu = torch.nn.ReLU()
        self.flatten = torch.nn.Flatten()
        self.linear1 = torch.nn.Linear(32, 64)
        self.conv = torch.nn.Conv2d(3, 6, kernel_size=(1, 1), stride=(1, 1))
        self.max_pooling2d = torch.nn.MaxPool2d(kernel_size=2)

    def forward(self, x):
        v1 = self.linear(x)
        v2 = v1.permute(0, 2, 1)
        v3 = self.flatten(v1)
        v4 = v3.reshape(v1.shape[0], 32, 1, 1)
        v5 = self.linear1(v3)
        v6 = v3.reshape(v5.shape[0], 6, 2, 2)
        v7 = self.conv(v6)
        v8 = self.relu(v3)
        v9 = self.max_pooling2d(v8)
        return v1.permute(0, 2, 1)



func = Model().to('cpu')


x1 = torch.randn(1, 2, 2)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (2x2 and 1x16)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., size=(1, 2, 2)), Parameter(FakeTensor(..., size=(16, 1), requires_grad=True)), Parameter(FakeTensor(..., size=(16,), requires_grad=True))), **{}):
a and b must have same reduction dim, but got [2, 2] X [1, 16].

from user code:
   File "<string>", line 25, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/linear.py", line 125, in forward
    return F.linear(input, self.weight, self.bias)


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''