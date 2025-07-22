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
        self.key = torch.nn.Linear(8, 16)
        self.query = torch.nn.Linear(8, 16)
        self.value = torch.nn.Linear(8, 16)

    def forward(self, x2):
        k = self.key(x2)
        q = self.query(x2)
        v = self.value(x2)
        qk = q @ k.transpose(-2, -1)
        return qk



func = Model().to('cpu')


x2 = torch.randn(1, 8, 10)

test_inputs = [x2]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (8x10 and 8x16)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., size=(1, 8, 10)), Parameter(FakeTensor(..., size=(16, 8), requires_grad=True)), Parameter(FakeTensor(..., size=(16,), requires_grad=True))), **{}):
a and b must have same reduction dim, but got [8, 10] X [8, 16].

from user code:
   File "<string>", line 22, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/linear.py", line 125, in forward
    return F.linear(input, self.weight, self.bias)


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''