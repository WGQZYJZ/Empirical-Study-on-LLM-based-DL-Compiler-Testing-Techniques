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
        self.linear = torch.nn.Linear(6, 1)

    def forward(self, x):
        (y0, y1) = x.chunk(2, dim=1)
        y2 = y0 - y1
        z = torch.cat([y0, y1, y2], dim=1)
        z = self.linear(z)
        (w, x, y) = z.chunk(3, dim=1)
        w = w + x
        return torch.relu(w + y)



func = Model().to('cpu')


x = torch.randn(2, 2, 2, 2)

test_inputs = [x]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (12x2 and 6x1)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., size=(2, 3, 2, 2)), Parameter(FakeTensor(..., size=(1, 6), requires_grad=True)), Parameter(FakeTensor(..., size=(1,), requires_grad=True))), **{}):
a and b must have same reduction dim, but got [12, 2] X [6, 1].

from user code:
   File "<string>", line 23, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/linear.py", line 125, in forward
    return F.linear(input, self.weight, self.bias)


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''