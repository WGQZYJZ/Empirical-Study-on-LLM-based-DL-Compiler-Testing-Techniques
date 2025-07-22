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
        self.seq = torch.nn.Sequential(torch.nn.Conv2d(28, 64, kernel_size=(3, 3), stride=1, padding=(1, 1)), torch.nn.MaxPool2d(2, stride=2, padding=0), torch.nn.Conv2d(64, 128, kernel_size=(3, 3), stride=1, padding=(1, 1)), torch.nn.MaxPool2d(2, stride=2, padding=0), torch.nn.Conv2d(128, 64, kernel_size=(3, 3), stride=1, padding=(1, 1)), torch.nn.MaxPool2d(2, stride=2, padding=0), torch.nn.Flatten(), torch.nn.Linear(576, 10))

    def forward(self, x1):
        v1 = self.seq(x1)
        v2 = torch.sigmoid(v1)
        return v2



func = Model().to('cpu')


x1 = torch.randn(1, 28, 32, 32)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (1x1024 and 576x10)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., size=(1, 64*((s1//8))*((s2//8)))), Parameter(FakeTensor(..., size=(10, 576), requires_grad=True)), Parameter(FakeTensor(..., size=(10,), requires_grad=True))), **{}):
a and b must have same reduction dim, but got [1, 64*((s1//8))*((s2//8))] X [576, 10].

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