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
        self.a = torch.nn.Linear(1280, 8)
        self.d = torch.nn.Conv2d(64, 64, kernel_size=(1, 1), stride=(1, 1))

    def forward(self, x):
        v = self.a(x)
        v = torch.mul(v, 1.0)
        v = torch.nn.functional.sigmoid(v)
        v = self.d(v)
        v = torch.nn.functional.relu(v)
        v = torch.nn.functional.leaky_relu(v, negative_slope=0.01)
        v = torch.nn.functional.softmax(v, dim=-1)
        return v



func = Model().to('cpu')


x = torch.randn(1, 8, 1, 8)

test_inputs = [x]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (8x8 and 1280x8)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., size=(1, 8, 1, 8)), Parameter(FakeTensor(..., size=(8, 1280), requires_grad=True)), Parameter(FakeTensor(..., size=(8,), requires_grad=True))), **{}):
a and b must have same reduction dim, but got [8, 8] X [1280, 8].

from user code:
   File "<string>", line 21, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/linear.py", line 125, in forward
    return F.linear(input, self.weight, self.bias)


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''