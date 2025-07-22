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

class Model(nn.Module):

    def __init__(self):
        super().__init__()
        self.layers1 = nn.Linear(2, 3)
        self.layers2 = nn.Linear(4, 2)
        self.layers3 = nn.Linear(6, 8)

    def forward(self, x):
        x = self.layers1(x)
        t1 = torch.cat((x, x))
        t2 = torch.cat((t1, t1))
        x = self.layers2(t2)
        x = self.layers3(x)
        return x



func = Model().to('cpu')


x = torch.randn(2, 2)

test_inputs = [x]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (8x3 and 4x2)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., size=(8, 3)), Parameter(FakeTensor(..., size=(2, 4), requires_grad=True)), Parameter(FakeTensor(..., size=(2,), requires_grad=True))), **{}):
a and b must have same reduction dim, but got [8, 3] X [4, 2].

from user code:
   File "<string>", line 25, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/linear.py", line 125, in forward
    return F.linear(input, self.weight, self.bias)


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''