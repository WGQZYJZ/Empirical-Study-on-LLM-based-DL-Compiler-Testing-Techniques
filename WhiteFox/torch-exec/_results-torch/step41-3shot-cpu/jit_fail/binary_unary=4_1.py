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
        self.linear1 = torch.nn.Linear(3, 5)
        self.linear2 = torch.nn.Linear(5, 6)

    def forward(self, x1, other):
        v1 = self.linear1(x1)
        v2 = v1 + other
        v3 = torch.nn.functional.relu(v2)
        v4 = self.linear2(v3)
        return v4


func = Model().to('cpu')


x1 = torch.randn(1, 3, 224, 224)

other = torch.randn(1, 5)

test_inputs = [x1, other]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (672x224 and 3x5)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., size=(1, 3, 224, 224)), Parameter(FakeTensor(..., size=(5, 3), requires_grad=True)), Parameter(FakeTensor(..., size=(5,), requires_grad=True))), **{}):
a and b must have same reduction dim, but got [672, 224] X [3, 5].

from user code:
   File "<string>", line 21, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/linear.py", line 125, in forward
    return F.linear(input, self.weight, self.bias)


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''