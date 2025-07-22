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

    def __init__(self, dim, num_heads):
        super().__init__()
        s = 7
        self.scale_factor = 1 / math.sqrt(dim)
        self.matmul1 = torch.nn.Linear(dim, num_heads * s)
        self.matmul2 = torch.nn.Linear(num_heads * s, dim)

    def forward(self, x1, x2, _=None):
        v1 = self.matmul1(x1)
        v2 = self.matmul2(x2)
        v3 = torch.matmul(x1, x2.transpose(-2, -1))
        v4 = v3 * self.scale_factor
        v5 = softmax(v4, dim=-1)
        v6 = drop_out(v5, 0.1)
        v7 = torch.matmul(v6.transpose(-2, -1), v2)
        return v7


dim = 1
num_heads = 1

func = Model(dim, num_heads).to('cpu')


x1 = torch.randn(1, 128, 3)

x2 = torch.randn(1, 128, 6)

test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (128x3 and 1x7)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., size=(1, 128, 3)), Parameter(FakeTensor(..., size=(7, 1), requires_grad=True)), Parameter(FakeTensor(..., size=(7,), requires_grad=True))), **{}):
a and b must have same reduction dim, but got [128, 3] X [1, 7].

from user code:
   File "<string>", line 23, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/linear.py", line 125, in forward
    return F.linear(input, self.weight, self.bias)


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''