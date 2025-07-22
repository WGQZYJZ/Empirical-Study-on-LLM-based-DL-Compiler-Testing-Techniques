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

    def __init__(self, n_channels, k, s, p):
        super().__init__()
        self.linear = torch.nn.Linear(n_channels, 16 * 16)

    def forward(self, x2):
        v2 = self.linear(x2)
        o2 = v2 - x2
        return o2


n_channels = 1
k = 1
s = 1
p = 1
func = Model(3, 1, 1, 1).to('cpu')


x2 = torch.randn(1, 3, 16, 16)

test_inputs = [x2]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (48x16 and 3x256)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., size=(1, 3, 16, 16)), Parameter(FakeTensor(..., size=(256, 3), requires_grad=True)), Parameter(FakeTensor(..., size=(256,), requires_grad=True))), **{}):
a and b must have same reduction dim, but got [48, 16] X [3, 256].

from user code:
   File "<string>", line 20, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/linear.py", line 125, in forward
    return F.linear(input, self.weight, self.bias)


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''