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
        self.layers = nn.Linear(16, 16)

    def forward(self, x):
        x = self.layers(x)
        x = torch.reshape(x, (-1, 4, 1, 2, 2))
        return x



func = Model().to('cpu')


x = torch.randn(1, 16, 1, 1, 1)

test_inputs = [x]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (16x1 and 16x16)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., size=(1, s0, 1, 1, 1)), Parameter(FakeTensor(..., size=(16, 16), requires_grad=True)), Parameter(FakeTensor(..., size=(16,), requires_grad=True))), **{}):
a and b must have same reduction dim, but got [s0, 1] X [16, 16].

from user code:
   File "<string>", line 20, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/linear.py", line 125, in forward
    return F.linear(input, self.weight, self.bias)


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''