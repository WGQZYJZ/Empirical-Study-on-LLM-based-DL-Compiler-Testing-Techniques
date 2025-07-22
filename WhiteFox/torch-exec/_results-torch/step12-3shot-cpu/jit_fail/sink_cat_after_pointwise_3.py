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
        self.conv1 = torch.nn.Conv2d(1, 20, 5, 1)
        self.bn1 = torch.nn.BatchNorm2d(20)
        self.relu = torch.nn.ReLU()
        self.conv2 = torch.nn.Conv2d(20, 50, 5, 1)
        self.bn2 = torch.nn.BatchNorm2d(50)
        self.max_pool2d = torch.nn.MaxPool2d(2, 2)
        self.view = lambda x: x.view(x.shape[0], -1)
        self.drop_out = torch.nn.Dropout()
        self.linear1 = torch.nn.Linear(4 * 4 * 50, 500)
        self.bn3 = torch.nn.BatchNorm1d(500)
        self.linear2 = torch.nn.Linear(500, 10)

    def forward(self, x):
        x = self.bn1(self.conv1(x))
        x = self.relu(x)
        x = self.max_pool2d(self.bn2(self.conv2(x)))
        x = self.view(x)
        x = self.drop_out(x)
        x = self.bn3(self.linear1(x))
        x = self.relu(x)
        x = self.linear2(x)
        return x



func = Model().to('cpu')


x = torch.randn(2, 1, 28, 28)

test_inputs = [x]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (2x5000 and 800x500)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., size=(2, 5000)), Parameter(FakeTensor(..., size=(500, 800), requires_grad=True)), Parameter(FakeTensor(..., size=(500,), requires_grad=True))), **{}):
a and b must have same reduction dim, but got [2, 5000] X [800, 500].

from user code:
   File "<string>", line 35, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/linear.py", line 125, in forward
    return F.linear(input, self.weight, self.bias)


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''