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
        self.f0 = torch.nn.Linear(5, 6)

    def forward(self, x1, x2):
        t1 = torch.cat([torch.mm(x1, x2), torch.mm(x1, x2)], 1)
        t2 = self.f0(t1)
        t3 = self.f0(t1)
        return torch.cat([t2, t3], 1)



func = Model().to('cpu')


x1 = torch.randn(3, 5)

x2 = torch.randn(5, 1)

test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (3x2 and 5x6)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., size=(3, 2)), Parameter(FakeTensor(..., size=(6, 5), requires_grad=True)), Parameter(FakeTensor(..., size=(6,), requires_grad=True))), **{}):
a and b must have same reduction dim, but got [3, 2] X [5, 6].

from user code:
   File "<string>", line 21, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/linear.py", line 125, in forward
    return F.linear(input, self.weight, self.bias)


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''