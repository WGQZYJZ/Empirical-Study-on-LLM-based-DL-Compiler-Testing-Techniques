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
        self.linear = torch.nn.Linear(81, 10)

    def forward(self, x1):
        x2 = x1.flatten(-2, -1)
        v1 = self.linear(x2)
        v2 = torch.sigmoid(v1)
        return v2


func = Model().to('cuda')


x1 = torch.randn(1, 7, 7)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (1x49 and 81x10)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., device='cuda:0', size=(1, s0*s1)), Parameter(FakeTensor(..., device='cuda:0', size=(10, 81), requires_grad=True)), Parameter(FakeTensor(..., device='cuda:0', size=(10,), requires_grad=True))), **{}):
a and b must have same reduction dim, but got [1, s0*s1] X [81, 10].

from user code:
   File "<string>", line 21, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/linear.py", line 125, in forward
    return F.linear(input, self.weight, self.bias)


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''