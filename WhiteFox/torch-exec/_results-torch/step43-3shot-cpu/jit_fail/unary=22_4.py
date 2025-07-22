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

    def __init__(self, input_size, output_size):
        super().__init__()
        self.layer = torch.nn.Linear(input_size, output_size)

    def forward(self, x1):
        v1 = self.layer(x1)
        v2 = torch.tanh(v1)
        return v2


input_size = 1
output_size = 1

func = Model(input_size, output_size).to('cpu')


x1 = torch.randn(1, 300)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (1x300 and 1x1)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., size=(1, s0)), Parameter(FakeTensor(..., size=(1, 1), requires_grad=True)), Parameter(FakeTensor(..., size=(1,), requires_grad=True))), **{}):
a and b must have same reduction dim, but got [1, s0] X [1, 1].

from user code:
   File "<string>", line 20, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/linear.py", line 125, in forward
    return F.linear(input, self.weight, self.bias)


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''