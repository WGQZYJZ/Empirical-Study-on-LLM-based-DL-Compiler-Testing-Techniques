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
        self.linear = torch.nn.Linear(64, 8)

    def forward(self, x1, x2):
        v1 = self.linear(x1)
        v2 = v1 - x2
        return v2


func = Model().to('cpu')


x1 = torch.randn(1, 8, 16, 16)

x2 = torch.randn(1, 8, 16, 16)

test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (128x16 and 64x8)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., size=(1, 8, 16, 16)), Parameter(FakeTensor(..., size=(8, 64), requires_grad=True)), Parameter(FakeTensor(..., size=(8,), requires_grad=True))), **{}):
a and b must have same reduction dim, but got [128, 16] X [64, 8].

from user code:
   File "<string>", line 20, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/linear.py", line 125, in forward
    return F.linear(input, self.weight, self.bias)


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''