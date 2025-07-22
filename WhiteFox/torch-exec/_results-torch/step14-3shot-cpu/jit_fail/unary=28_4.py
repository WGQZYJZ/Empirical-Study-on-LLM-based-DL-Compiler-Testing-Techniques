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
        self.l1 = torch.nn.Linear(3072, 768, bias=True)

    def forward(self, x):
        v0 = torch.flatten(x, 1)
        v1 = self.l1(v0)
        v2 = torch.clamp_min(v1, min=-0.2514298553466797)
        v3 = torch.clamp_max(v2, max=0.5333021664619446)
        return v3


func = Model().to('cpu')


x_dummy = torch.randn(1, 3, 64, 64)

test_inputs = [x_dummy]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (1x12288 and 3072x768)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., size=(1, 12288)), Parameter(FakeTensor(..., size=(768, 3072), requires_grad=True)), Parameter(FakeTensor(..., size=(768,), requires_grad=True))), **{}):
a and b must have same reduction dim, but got [1, 12288] X [3072, 768].

from user code:
   File "<string>", line 21, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/linear.py", line 125, in forward
    return F.linear(input, self.weight, self.bias)


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''