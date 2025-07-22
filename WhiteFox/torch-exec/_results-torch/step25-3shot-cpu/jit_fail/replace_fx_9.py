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
        self.dropout1 = torch.nn.Dropout2d(p=0.25)
        self.avgpool1 = torch.nn.AvgPool2d(2, stride=2)
        self.dropout2 = torch.nn.Dropout2d(p=0.5)
        self.fc1 = torch.nn.Linear(4480, 120)
        self.fc2 = torch.nn.Linear(120, 84)
        self.dropout3 = torch.nn.Dropout2d(p=0.25)
        self.fc3 = torch.nn.Linear(84, 10)

    def forward(self, x1):
        x2 = self.conv1(x1)
        x3 = self.dropout1(x2)
        x4 = self.avgpool1(x3)
        x5 = self.dropout2(x4)
        x6 = torch.flatten(x5, 1)
        x7 = self.fc1(x6)
        x8 = self.fc2(x7)
        x9 = self.dropout3(x7)
        x10 = self.fc3(x9)
        return (x2, x9, x10)



func = Model().to('cpu')


x1 = torch.randn(1, 100, 100)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (20x2304 and 4480x120)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., size=(20, 2304)), Parameter(FakeTensor(..., size=(120, 4480), requires_grad=True)), Parameter(FakeTensor(..., size=(120,), requires_grad=True))), **{}):
a and b must have same reduction dim, but got [20, 2304] X [4480, 120].

from user code:
   File "<string>", line 32, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/linear.py", line 125, in forward
    return F.linear(input, self.weight, self.bias)


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''