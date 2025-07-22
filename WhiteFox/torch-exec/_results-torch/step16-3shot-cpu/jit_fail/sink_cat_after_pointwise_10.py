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
        self.relu = torch.nn.ReLU()
        self.model1 = torch.nn.Sequential()
        self.model1.add_module('conv1', torch.nn.Conv2d(1, 20, 5, 1))
        self.model1.add_module('pool1', torch.nn.MaxPool2d(2, 2))
        self.model1.add_module('conv2', torch.nn.Conv2d(20, 50, 5, 1))
        self.model1.add_module('pool2', torch.nn.MaxPool2d(2, 2))
        self.model1.add_module('fc1', torch.nn.Linear(4 * 4 * 50, 500))
        self.model1.add_module('relu1', torch.nn.ReLU())
        self.model1.add_module('fc2', torch.nn.Linear(500, 84))
        self.tanh = torch.nn.Tanh()

    def forward(self, x):
        y = self.model1(x)
        y = self.tanh(y)
        return y



func = Model().to('cpu')


x = torch.randn(1, 1, 28, 28)

test_inputs = [x]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (200x4 and 800x500)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., size=(1, 50, 4, 4)), Parameter(FakeTensor(..., size=(500, 800), requires_grad=True)), Parameter(FakeTensor(..., size=(500,), requires_grad=True))), **{}):
a and b must have same reduction dim, but got [200, 4] X [800, 500].

from user code:
   File "<string>", line 29, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/container.py", line 250, in forward
    input = module(input)
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/linear.py", line 125, in forward
    return F.linear(input, self.weight, self.bias)


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''