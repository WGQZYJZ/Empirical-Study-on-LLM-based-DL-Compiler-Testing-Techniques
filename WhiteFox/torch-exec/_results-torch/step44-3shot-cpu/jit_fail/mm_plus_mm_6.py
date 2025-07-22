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
        self.linear1 = torch.nn.Linear(1, 1)
        self.linear2 = torch.nn.Linear(1, 1)
        self.linear3 = torch.nn.Linear(1, 1)
        self.linear4 = torch.nn.Linear(1, 1)

    def forward(self, input1, input2, input3):
        x1 = input1
        x2 = input2
        x3 = input3
        x4 = input1
        x1 = torch.mm(x1, x4)
        x2 = self.linear1(input1)
        x3 = torch.mm(x2, x1)
        x4 = self.linear2(x3)
        x1 = torch.mm(x2, input2)
        x2 = self.linear3(x1)
        x3 = self.linear3(x2)
        x4 = torch.mm(x3, input3)
        x1 = self.linear3(x3)
        x2 = self.linear4(x1)
        x3 = x4 + x2
        return x2 + x3 + x3



func = Model().to('cpu')


input1 = torch.randn(4, 4)

input2 = torch.randn(4, 4)

input3 = torch.randn(4, 4)

test_inputs = [input1, input2, input3]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (4x4 and 1x1)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., size=(4, 4)), Parameter(FakeTensor(..., size=(1, 1), requires_grad=True)), Parameter(FakeTensor(..., size=(1,), requires_grad=True))), **{}):
a and b must have same reduction dim, but got [4, 4] X [1, 1].

from user code:
   File "<string>", line 28, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/linear.py", line 125, in forward
    return F.linear(input, self.weight, self.bias)


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''