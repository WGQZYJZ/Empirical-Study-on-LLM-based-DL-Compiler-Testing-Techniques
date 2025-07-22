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
        self.linear = torch.nn.Linear(10, 20)

    def forward(self, x2, other):
        v1 = self.linear(x2)
        v2 = v1 + other
        v3 = torch.relu(v2)
        return v3


func = Model().to('cpu')


other = torch.randn(20, 500)

x2 = torch.randn(10, 500)

test_inputs = [other, x2]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (20x500 and 10x20)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., size=(20, 500)), Parameter(FakeTensor(..., size=(20, 10), requires_grad=True)), Parameter(FakeTensor(..., size=(20,), requires_grad=True))), **{}):
a and b must have same reduction dim, but got [20, 500] X [10, 20].

from user code:
   File "<string>", line 20, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/linear.py", line 125, in forward
    return F.linear(input, self.weight, self.bias)


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''