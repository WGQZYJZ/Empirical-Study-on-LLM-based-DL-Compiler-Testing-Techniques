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
        self.linear = torch.nn.Linear(32, 8)

    def forward(self, x1, x2):
        x = torch.cat((x1, x2), axis=1)
        v1 = self.linear(x)
        v2 = v1 - x2
        return v2


func = Model().to('cpu')


x1 = torch.randn(2, 32)

x2 = torch.randn(2, 32)

test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (2x64 and 32x8)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., size=(s0, s1 + s3)), Parameter(FakeTensor(..., size=(8, 32), requires_grad=True)), Parameter(FakeTensor(..., size=(8,), requires_grad=True))), **{}):
a and b must have same reduction dim, but got [s0, s1 + s3] X [32, 8].

from user code:
   File "<string>", line 21, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/linear.py", line 125, in forward
    return F.linear(input, self.weight, self.bias)


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''