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
        self.linear = torch.nn.Linear(12544, 25088)

    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 > 0
        negative_slope = 0.2
        v3 = negative_slope * v1
        v4 = torch.where(v2, v1, v3)
        return v4


func = Model().to('cpu')


x1 = torch.randn(1, 25088)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (1x25088 and 12544x25088)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., size=(1, s0)), Parameter(FakeTensor(..., size=(25088, 12544), requires_grad=True)), Parameter(FakeTensor(..., size=(25088,), requires_grad=True))), **{}):
a and b must have same reduction dim, but got [1, s0] X [12544, 25088].

from user code:
   File "<string>", line 20, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/linear.py", line 125, in forward
    return F.linear(input, self.weight, self.bias)


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''