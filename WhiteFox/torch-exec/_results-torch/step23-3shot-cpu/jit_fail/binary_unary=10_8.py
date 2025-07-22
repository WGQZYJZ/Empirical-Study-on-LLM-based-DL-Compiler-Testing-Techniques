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
        self.linear1 = torch.nn.Linear(1000, 4096)
        self.linear2 = torch.nn.Linear(4096, 4096)
        self.linear3 = torch.nn.Linear(4096, 7)

    def forward(self, x1, x2, x3):
        t1 = self.linear1(x1)
        t2 = self.linear2(x2)
        t3 = self.linear3(x3)
        cat1 = torch.cat((t1, t2), 1)
        cat2 = torch.cat((cat1, t3), 1)
        return cat2


func = Model().to('cpu')


x1 = torch.randn(1000)

x2 = torch.randn(1000)

x3 = torch.randn(7)

test_inputs = [x1, x2, x3]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (1x1000 and 4096x4096)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., size=(1000,)), Parameter(FakeTensor(..., size=(4096, 4096), requires_grad=True)), Parameter(FakeTensor(..., size=(4096,), requires_grad=True))), **{}):
a and b must have same reduction dim, but got [1, 1000] X [4096, 4096].

from user code:
   File "<string>", line 23, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/linear.py", line 125, in forward
    return F.linear(input, self.weight, self.bias)


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''