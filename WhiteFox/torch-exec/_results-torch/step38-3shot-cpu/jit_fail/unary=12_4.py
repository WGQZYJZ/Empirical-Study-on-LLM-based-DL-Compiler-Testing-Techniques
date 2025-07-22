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
        self.layers = torch.nn.Sequential(torch.nn.Conv2d(3, 4, 5, stride=1, padding=2), torch.nn.ReLU(True), torch.nn.MaxPool2d(kernel_size=2, stride=2), torch.nn.BatchNorm2d(4), torch.nn.Conv2d(4, 8, 10, stride=1, padding=4), torch.nn.ReLU(True), torch.nn.MaxPool2d(kernel_size=2, stride=2), torch.nn.BatchNorm2d(8), torch.nn.Flatten(), torch.nn.Linear(1024, 20), torch.nn.ReLU(True), torch.nn.BatchNorm1d(20), torch.nn.Linear(20, 3), torch.nn.Softmax())

    def forward(self, x1):
        v1 = self.layers(x1)
        return v1



func = Model().to('cpu')


x1 = torch.randn(1, 3, 64, 64)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (1x1800 and 1024x20)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(...,
           size=(1, 8*((((((s0//2)) - 3)//2)) + 1)*((((((s1//2)) - 3)//2)) + 1))), Parameter(FakeTensor(..., size=(20, 1024), requires_grad=True)), Parameter(FakeTensor(..., size=(20,), requires_grad=True))), **{}):
a and b must have same reduction dim, but got [1, 8*((((((s0//2)) - 3)//2)) + 1)*((((((s1//2)) - 3)//2)) + 1)] X [1024, 20].

from user code:
   File "<string>", line 20, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/container.py", line 250, in forward
    input = module(input)
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/linear.py", line 125, in forward
    return F.linear(input, self.weight, self.bias)


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''