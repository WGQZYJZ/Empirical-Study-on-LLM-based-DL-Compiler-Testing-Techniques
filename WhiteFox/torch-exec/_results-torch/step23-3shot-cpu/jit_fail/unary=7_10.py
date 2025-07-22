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
        self.linear_relu6 = torch.nn.Sequential(torch.nn.Linear(3, 4), torch.nn.ReLU6(inplace=True))

    def forward(self, x2):
        j1 = self.linear_relu6(x2)
        q1 = j1 * torch.clamp(j1 + 3, min=0, max=6)
        y = q1 / 6
        return y


func = Model().to('cpu')


x2 = torch.randn(1, 3, 2)

test_inputs = [x2]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (3x2 and 3x4)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., size=(1, 3, 2)), Parameter(FakeTensor(..., size=(4, 3), requires_grad=True)), Parameter(FakeTensor(..., size=(4,), requires_grad=True))), **{}):
a and b must have same reduction dim, but got [3, 2] X [3, 4].

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