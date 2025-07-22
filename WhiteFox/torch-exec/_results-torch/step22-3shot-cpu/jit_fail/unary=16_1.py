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
        self.fc1 = torch.nn.Linear(3 * 64 * 64, 30)
        self.maxpool = torch.nn.MaxPool2d(kernel_size=2, stride=2)

    def forward(self, x1):
        fc1 = self.maxpool(F.relu(self.fc1(x1)))
        h1 = torch.flatten(fc1, start_dim=1)
        return h1


func = Model().to('cpu')


x1 = torch.randn(1, 3, 64, 64)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (192x64 and 12288x30)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., size=(1, 3, s0, s1)), Parameter(FakeTensor(..., size=(30, 12288), requires_grad=True)), Parameter(FakeTensor(..., size=(30,), requires_grad=True))), **{}):
a and b must have same reduction dim, but got [3*s0, s1] X [12288, 30].

from user code:
   File "<string>", line 21, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/linear.py", line 125, in forward
    return F.linear(input, self.weight, self.bias)


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''