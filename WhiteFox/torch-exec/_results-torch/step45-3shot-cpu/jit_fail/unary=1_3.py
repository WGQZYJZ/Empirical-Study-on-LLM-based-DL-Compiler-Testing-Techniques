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
        self.linear = torch.nn.Linear(16, 16)

    def forward(self, input_tensor):
        x1 = self.linear(input_tensor)
        x2 = x1 * 0.5
        x3 = x1 + x1 * x1 * x1 * 0.044715
        x5 = torch.tanh(x3)
        x6 = x5 + 1
        x7 = x2 * x6
        return x7


func = Model().to('cpu')


input_tensor = torch.randn(2, 16, 5, 5)

test_inputs = [input_tensor]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (160x5 and 16x16)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., size=(2, 16, 5, 5)), Parameter(FakeTensor(..., size=(16, 16), requires_grad=True)), Parameter(FakeTensor(..., size=(16,), requires_grad=True))), **{}):
a and b must have same reduction dim, but got [160, 5] X [16, 16].

from user code:
   File "<string>", line 20, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/linear.py", line 125, in forward
    return F.linear(input, self.weight, self.bias)


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''