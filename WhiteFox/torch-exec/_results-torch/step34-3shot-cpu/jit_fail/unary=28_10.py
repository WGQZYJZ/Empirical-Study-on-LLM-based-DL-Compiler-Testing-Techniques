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

    def __init__(self, min_value, max_value):
        super().__init__()
        self.linear = torch.nn.Linear(2, 7)

    def forward(self, x):
        w1 = self.linear(x)
        w2 = torch.clamp_min(w1, min_value=self.min_value)
        w3 = torch.clamp_max(w2, max_value=self.max_value)
        return w3


min_value = 1
max_value = 1
func = Model(3.1, 4.1).to('cpu')


x = torch.randn(7, 2, 11, 13)

test_inputs = [x]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (154x13 and 2x7)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., size=(7, 2, 11, 13)), Parameter(FakeTensor(..., size=(7, 2), requires_grad=True)), Parameter(FakeTensor(..., size=(7,), requires_grad=True))), **{}):
a and b must have same reduction dim, but got [154, 13] X [2, 7].

from user code:
   File "<string>", line 20, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/linear.py", line 125, in forward
    return F.linear(input, self.weight, self.bias)


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''