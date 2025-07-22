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
        self.branch1 = torch.nn.Sequential(torch.nn.Conv2d(2, 3, 2, stride=1), torch.nn.Linear(3 * 10 * 10, 4))
        self.branch2 = torch.nn.Sequential(torch.nn.Conv2d(2, 3, 2), torch.nn.Linear(15 * 5 * 5, 4))

    def forward(self, x):
        a = self.branch1(x)
        b = self.branch2(x)
        return torch.cat((a, torch.relu(b), torch.relu(a), b, torch.relu(a)), dim=1)



func = Model().to('cpu')


x = torch.randn(1, 2, 3, 3)

test_inputs = [x]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (6x2 and 300x4)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., size=(1, 3, 2, 2)), Parameter(FakeTensor(..., size=(4, 300), requires_grad=True)), Parameter(FakeTensor(..., size=(4,), requires_grad=True))), **{}):
a and b must have same reduction dim, but got [6, 2] X [300, 4].

from user code:
   File "<string>", line 21, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/container.py", line 250, in forward
    input = module(input)
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/linear.py", line 125, in forward
    return F.linear(input, self.weight, self.bias)


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''