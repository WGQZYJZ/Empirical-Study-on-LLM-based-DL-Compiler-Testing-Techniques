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

    def __init__(self, n, d, h, s, p):
        super().__init__()
        self.dense1 = torch.nn.Linear(n, d)
        self.dense2 = torch.nn.Linear(d, h)
        self.dense3 = torch.nn.Linear(h, n)
        self.softmax = torch.nn.Softmax(dim=-1)
        self.dropout = torch.nn.Dropout(p)

    def forward(self, x):
        v1 = self.dense1(x)
        v2 = self.dense2(v1)
        v3 = self.dense3(v2)
        v4 = self.dropout(self.softmax(v3 * 10))
        v5 = v3.mm(v4.transpose(0, 1))
        return v5


n = 1
d = 1
h = 1
s = 1
p = 1

func = Model(n, d, h, s, p).to('cpu')


x1 = torch.randn(4, 5)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (4x5 and 1x1)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., size=(4, 5)), Parameter(FakeTensor(..., size=(1, 1), requires_grad=True)), Parameter(FakeTensor(..., size=(1,), requires_grad=True))), **{}):
a and b must have same reduction dim, but got [4, 5] X [1, 1].

from user code:
   File "<string>", line 24, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/linear.py", line 125, in forward
    return F.linear(input, self.weight, self.bias)


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''