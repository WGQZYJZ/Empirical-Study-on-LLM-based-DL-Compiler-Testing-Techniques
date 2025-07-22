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
        self.linear_1 = torch.nn.Linear(21, 21)
        self.linear_2 = torch.nn.Linear(21, 5)
        self.linear_3 = torch.nn.Linear(5, 16)

    def forward(self, x):
        x = self.linear_1(x)
        x = self.linear_2(x)
        x = self.linear_3(x)
        x = torch.relu(x)
        return x



func = Model().to('cpu')


x1 = torch.randn(1, 70)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (1x70 and 21x21)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., size=(1, 70)), Parameter(FakeTensor(..., size=(21, 21), requires_grad=True)), Parameter(FakeTensor(..., size=(21,), requires_grad=True))), **{}):
a and b must have same reduction dim, but got [1, 70] X [21, 21].

from user code:
   File "<string>", line 22, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/linear.py", line 125, in forward
    return F.linear(input, self.weight, self.bias)


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''