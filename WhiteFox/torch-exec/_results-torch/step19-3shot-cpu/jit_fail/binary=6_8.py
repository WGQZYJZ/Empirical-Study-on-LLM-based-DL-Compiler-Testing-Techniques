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
        self.linear = torch.nn.Linear(512, 512)

    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 - 2
        return v2


func = Model().to('cpu')


x1 = torch.randn(1, 512, 7, 7)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (3584x7 and 512x512)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., size=(1, s0, s1, s2)), Parameter(FakeTensor(..., size=(512, 512), requires_grad=True)), Parameter(FakeTensor(..., size=(512,), requires_grad=True))), **{}):
a and b must have same reduction dim, but got [s0*s1, s2] X [512, 512].

from user code:
   File "<string>", line 20, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/linear.py", line 125, in forward
    return F.linear(input, self.weight, self.bias)


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''