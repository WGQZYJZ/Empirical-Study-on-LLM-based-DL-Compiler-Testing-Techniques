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
        if False:
            self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        else:
            self.linear = torch.nn.Linear(8 * 64 * 64, 1)

    def forward(self, x1):
        if False:
            v1 = self.conv(x1)
        else:
            v1 = self.linear(torch.flatten(x1, start_dim=1))
        v2 = v1 * 0.5
        v3 = v1 * 0.7071067811865476
        v4 = torch.erf(v3)
        v5 = v4 + 1
        v6 = v2 * v5
        return v6


func = Model().to('cpu')


x1 = torch.randn(1, 3, 64, 64)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (1x12288 and 32768x1)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., size=(1, 12288)), Parameter(FakeTensor(..., size=(1, 32768), requires_grad=True)), Parameter(FakeTensor(..., size=(1,), requires_grad=True))), **{}):
a and b must have same reduction dim, but got [1, 12288] X [32768, 1].

from user code:
   File "<string>", line 26, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/linear.py", line 125, in forward
    return F.linear(input, self.weight, self.bias)


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''