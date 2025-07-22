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
        self.p1 = torch.nn.Parameter(torch.randn(32))
        self.p2 = torch.nn.Parameter(torch.randn(32))
        self.p3 = torch.nn.Parameter(torch.randn(32))
        self.p4 = torch.nn.Parameter(torch.randn(32))
        self.w1 = torch.nn.Linear(1, 32)
        self.w2 = torch.nn.Linear(3, 16)
        self.w3 = torch.nn.Linear(16, 8)

    def forward(self, x1, x2):
        w1 = self.w1(x1)
        w2 = self.w2(x2).unsqueeze(dim=1)
        w3 = self.w3(w1 + self.p1) + self.p2 @ w2
        w4 = self.w1(x1) @ self.p4.unsqueeze(dim=0)
        return w3 + w4



func = Model().to('cpu')


x1 = torch.randn(4, 1)

x2 = torch.randn(4, 3)

test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (4x32 and 16x8)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., size=(4, 32)), Parameter(FakeTensor(..., size=(8, 16), requires_grad=True)), Parameter(FakeTensor(..., size=(8,), requires_grad=True))), **{}):
a and b must have same reduction dim, but got [4, 32] X [16, 8].

from user code:
   File "<string>", line 28, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/linear.py", line 125, in forward
    return F.linear(input, self.weight, self.bias)


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''