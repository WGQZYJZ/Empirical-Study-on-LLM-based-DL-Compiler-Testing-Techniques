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

    def __init__(self, negative_slope):
        super().__init__()
        self.linear = torch.nn.Linear(256, 512)
        self.negative_slope = negative_slope

    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 > 0
        v3 = v1 * self.negative_slope
        v4 = torch.where(v2, v1, v3)
        return v4


negative_slope = 1
func = Model(0.1).to('cpu')


x1 = torch.randn(256, 3, 3, 3)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (2304x3 and 256x512)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., size=(256, 3, 3, 3)), Parameter(FakeTensor(..., size=(512, 256), requires_grad=True)), Parameter(FakeTensor(..., size=(512,), requires_grad=True))), **{}):
a and b must have same reduction dim, but got [2304, 3] X [256, 512].

from user code:
   File "<string>", line 21, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/linear.py", line 125, in forward
    return F.linear(input, self.weight, self.bias)


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''