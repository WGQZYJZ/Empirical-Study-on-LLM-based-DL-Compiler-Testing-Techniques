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
        self.l5 = torch.nn.Linear(10, 20, bias=False)

    def forward(self, x1):
        l1 = x1.mean(dim=[-1], keepdims=True)
        l2 = self.l5(l1)
        l3 = l2 + 3
        l4 = torch.clamp_min(l3, 0)
        l5 = torch.clamp_max(l4, 6)
        return l5


func = Model().to('cpu')


x1 = torch.randn(32, 10)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (32x1 and 10x20)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., size=(s0, 1)), Parameter(FakeTensor(..., size=(20, 10), requires_grad=True)), None), **{}):
a and b must have same reduction dim, but got [s0, 1] X [10, 20].

from user code:
   File "<string>", line 21, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/linear.py", line 125, in forward
    return F.linear(input, self.weight, self.bias)


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''