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
        self.t1 = torch.nn.ConvTranspose2d(7, 10, 1)
        self.t2 = torch.nn.Linear(10, 1)

    def forward(self, x1):
        v1 = self.t2(self.t1(x1))
        v2 = torch.relu(v1)
        return v2



func = Model().to('cpu')


x1 = torch.randn(1, 7, 15, 15)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (150x15 and 10x1)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., size=(1, 10, 15, 15)), Parameter(FakeTensor(..., size=(1, 10), requires_grad=True)), Parameter(FakeTensor(..., size=(1,), requires_grad=True))), **{}):
a and b must have same reduction dim, but got [150, 15] X [10, 1].

from user code:
   File "<string>", line 21, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/linear.py", line 125, in forward
    return F.linear(input, self.weight, self.bias)


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''