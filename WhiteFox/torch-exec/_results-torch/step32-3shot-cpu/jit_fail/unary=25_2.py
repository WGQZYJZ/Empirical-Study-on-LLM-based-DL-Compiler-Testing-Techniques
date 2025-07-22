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
        self.linear = torch.nn.Linear(8, 32, bias=True)
        self.lrelu = torch.nn.LeakyReLU(-0.5)

    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 > 0
        v3 = v1 * -0.5
        v4 = torch.where(v2, v1, v3)
        return self.lrelu(v4)


func = Model().to('cpu')


x1 = torch.randn(7, 8, 4, 4)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (224x4 and 8x32)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., size=(7, 8, 4, 4)), Parameter(FakeTensor(..., size=(32, 8), requires_grad=True)), Parameter(FakeTensor(..., size=(32,), requires_grad=True))), **{}):
a and b must have same reduction dim, but got [224, 4] X [8, 32].

from user code:
   File "<string>", line 21, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/linear.py", line 125, in forward
    return F.linear(input, self.weight, self.bias)


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''