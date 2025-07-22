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
        self.linear1 = torch.nn.Linear(25, 50)

    def forward(self, x1, x2):
        v1 = torch.matmul(x1, x2)
        v2 = self.linear1(v1)
        v3 = torch.cat([v1, v2], dim=1)
        return v3


func = Model().to('cuda')


x1 = torch.randn(8, 25)

x2 = torch.randn(25, 50)

test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (8x50 and 25x50)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., device='cuda:0', size=(8, 50)), Parameter(FakeTensor(..., device='cuda:0', size=(50, 25), requires_grad=True)), Parameter(FakeTensor(..., device='cuda:0', size=(50,), requires_grad=True))), **{}):
a and b must have same reduction dim, but got [8, 50] X [25, 50].

from user code:
   File "<string>", line 21, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/linear.py", line 125, in forward
    return F.linear(input, self.weight, self.bias)


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''