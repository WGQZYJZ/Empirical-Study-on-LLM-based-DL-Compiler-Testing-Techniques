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

    def __init__(self, i1, i2):
        super().__init__()
        self.linear = torch.nn.Linear(i1, i2)

    def forward(self, x2):
        v2 = self.linear(x2)
        v3 = v2 * 0.5
        v4 = v2 + v2 * v2 * v2 * 0.044715
        v5 = v4 * 0.7978845608028654
        v6 = torch.tanh(v5)
        v7 = v6 + 1
        v8 = v3 * v7
        return v8


i1 = 1
i2 = 1

func = Model(i1, i2).to('cpu')

__i_s__ = (2048, 2048)

__i_s__ = (2048, 2048)
x2 = torch.randn(1, *__i_s__)

test_inputs = [x2]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (2048x2048 and 1x1)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., size=(1, 2048, 2048)), Parameter(FakeTensor(..., size=(1, 1), requires_grad=True)), Parameter(FakeTensor(..., size=(1,), requires_grad=True))), **{}):
a and b must have same reduction dim, but got [2048, 2048] X [1, 1].

from user code:
   File "<string>", line 20, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/linear.py", line 125, in forward
    return F.linear(input, self.weight, self.bias)


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''