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
        self.linear = torch.nn.Linear(64 * 64, 256)

    def forward(self, x1):
        v1 = self.linear(x1.view(-1))
        v2 = v1 * 0.5
        v3 = v1 * 0.7071067811865476
        v4 = torch.erf(v3)
        v5 = v4 + 1
        v6 = v2 * v5
        return v6


func = Model().to('cuda')


x1 = torch.randn(1, 3, 64, 64)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (1x12288 and 4096x256)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., device='cuda:0', size=(s0*s1*s2,)), Parameter(FakeTensor(..., device='cuda:0', size=(256, 4096), requires_grad=True)), Parameter(FakeTensor(..., device='cuda:0', size=(256,), requires_grad=True))), **{}):
a and b must have same reduction dim, but got [1, s0*s1*s2] X [4096, 256].

from user code:
   File "<string>", line 20, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/linear.py", line 125, in forward
    return F.linear(input, self.weight, self.bias)


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''