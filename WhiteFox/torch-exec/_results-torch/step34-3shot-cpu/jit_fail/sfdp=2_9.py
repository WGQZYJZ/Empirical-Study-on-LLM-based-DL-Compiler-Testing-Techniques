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
        self.fc1 = torch.nn.Linear(10, 24)
        self.fc2 = torch.nn.Linear(24, 8)

    def forward(self, x1, x2):
        v1 = self.fc1(x1)
        v2 = self.fc2(v1)
        v3 = torch.matmul(x2, v2.transpose(1, 0))
        v4 = v3.softmax(dim=-1)
        v5 = v4.dropout(p=0)
        return v5.matmul(v1)


func = Model().to('cpu')


x1 = torch.randn(10, 10, 1)

x2 = torch.randn(20, 10, 1)

test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (100x1 and 10x24)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., size=(10, 10, 1)), Parameter(FakeTensor(..., size=(24, 10), requires_grad=True)), Parameter(FakeTensor(..., size=(24,), requires_grad=True))), **{}):
a and b must have same reduction dim, but got [100, 1] X [10, 24].

from user code:
   File "<string>", line 21, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/linear.py", line 125, in forward
    return F.linear(input, self.weight, self.bias)


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''