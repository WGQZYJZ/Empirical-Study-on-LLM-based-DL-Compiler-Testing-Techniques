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

    def __init__(self, dim, input_size, output_size):
        super().__init__()
        self.linear = torch.nn.Linear(input_size, output_size)

    def forward(self, x2):
        v7 = self.linear(x2)
        v8 = torch.nn.functional.relu(v7)
        return v8


dim = 1
input_size = 1
output_size = 1

func = Model(dim, input_size, output_size).to('cpu')


x2 = torch.randn(10, 8)

test_inputs = [x2]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (10x8 and 1x1)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., size=(10, 8)), Parameter(FakeTensor(..., size=(1, 1), requires_grad=True)), Parameter(FakeTensor(..., size=(1,), requires_grad=True))), **{}):
a and b must have same reduction dim, but got [10, 8] X [1, 1].

from user code:
   File "<string>", line 20, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/linear.py", line 125, in forward
    return F.linear(input, self.weight, self.bias)


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''