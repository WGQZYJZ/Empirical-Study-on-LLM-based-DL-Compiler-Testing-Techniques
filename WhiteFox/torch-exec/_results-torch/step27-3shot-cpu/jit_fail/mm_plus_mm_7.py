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
        super(Model, self).__init__()
        self.d1 = torch.nn.Linear(in_features=256, out_features=16)
        self.d2 = torch.nn.Linear(in_features=16, out_features=6)
        self.d3 = torch.nn.Linear(in_features=16, out_features=16)
        self.d4 = torch.nn.Linear(in_features=6, out_features=16)
        self.d5 = torch.nn.Linear(in_features=16, out_features=16)
        self.d6 = torch.nn.Linear(in_features=16, out_features=16)
        self.d7 = torch.nn.Linear(in_features=16, out_features=16)
        self.d8 = torch.nn.Linear(in_features=16, out_features=1)

    def forward(self, x1, x2, x3, x4):
        hidden1 = self.d2(self.d1(x2))
        hidden2 = self.d3(self.d4(hidden1))
        hidden3 = self.d5(self.d6(self.d7(hidden2)))
        hidden3 = self.d5(self.d6(self.d7(hidden2)))
        hidden4 = self.d1(self.d8(x3))
        hidden5 = self.d1(self.d8(x1))
        hidden6 = torch.mm(hidden4, hidden5)
        return hidden6



func = Model().to('cpu')


x1 = torch.randn(18, 256)

x2 = torch.randn(18, 256)

x3 = torch.randn(25, 1)

x4 = torch.randn(25, 6)

test_inputs = [x1, x2, x3, x4]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (25x1 and 16x1)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., size=(25, 1)), Parameter(FakeTensor(..., size=(1, 16), requires_grad=True)), Parameter(FakeTensor(..., size=(1,), requires_grad=True))), **{}):
a and b must have same reduction dim, but got [25, 1] X [16, 1].

from user code:
   File "<string>", line 31, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/linear.py", line 125, in forward
    return F.linear(input, self.weight, self.bias)


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''