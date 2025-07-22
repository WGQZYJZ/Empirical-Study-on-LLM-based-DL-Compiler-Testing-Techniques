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
        self.conv_transpose = torch.nn.ConvTranspose2d(1, 4, 5, stride=2, padding=2, dilation=1)
        self.linear = torch.nn.Linear(4, 5)

    def forward(self, x1, x2):
        v1 = self.conv_transpose(x1)
        v2 = self.linear(v1)
        return v2



func = Model().to('cpu')


x1 = torch.randn(1, 1, 32, 32)

x2 = torch.randn(1, 5, 1)

test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (252x63 and 4x5)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., size=(1, 4, 2*s0 - 1, 2*s1 - 1)), Parameter(FakeTensor(..., size=(5, 4), requires_grad=True)), Parameter(FakeTensor(..., size=(5,), requires_grad=True))), **{}):
a and b must have same reduction dim, but got [8*s0 - 4, 2*s1 - 1] X [4, 5].

from user code:
   File "<string>", line 22, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/linear.py", line 125, in forward
    return F.linear(input, self.weight, self.bias)


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''