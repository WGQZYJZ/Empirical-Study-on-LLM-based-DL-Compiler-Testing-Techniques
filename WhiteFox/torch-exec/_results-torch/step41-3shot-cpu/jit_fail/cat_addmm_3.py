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

class Model(nn.Module):

    def __init__(self):
        super().__init__()
        self.layers = nn.Linear(10, 5)

    def forward(self, x):
        input = torch.cat((x, x, x, x, x, x, x, x, x, x), dim=1)
        x = self.layers(input)
        return x



func = Model().to('cpu')


x = torch.randn(2, 10)

test_inputs = [x]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (2x100 and 10x5)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., size=(2, 100)), Parameter(FakeTensor(..., size=(5, 10), requires_grad=True)), Parameter(FakeTensor(..., size=(5,), requires_grad=True))), **{}):
a and b must have same reduction dim, but got [2, 100] X [10, 5].

from user code:
   File "<string>", line 21, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/linear.py", line 125, in forward
    return F.linear(input, self.weight, self.bias)


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''