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
        self.linear = torch.nn.Linear(16, 8, bias=False)
        self.other = torch.tensor([1, 2, 3, 4, 5, 6, 7, 8]).float().view(1, 2, 4)

    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 - self.other
        return v2


func = Model().to('cpu')


x1 = torch.randn(1, 16, 32)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (16x32 and 16x8)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., size=(1, 16, 32)), Parameter(FakeTensor(..., size=(8, 16), requires_grad=True)), None), **{}):
a and b must have same reduction dim, but got [16, 32] X [16, 8].

from user code:
   File "<string>", line 21, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/linear.py", line 125, in forward
    return F.linear(input, self.weight, self.bias)


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''