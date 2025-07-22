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
        self.layers = nn.Linear(2, 4)
        self.layers0 = nn.Linear(4, 9)
        self.layers1 = nn.Linear(9, 7)

    def forward(self, x):
        x = self.layers(x)
        x = torch.cat((x, x, x), dim=1)
        x = self.layers0(x)
        x = torch.cat((x, x, x), dim=1)
        x = self.layers1(x)
        return x



func = Model().to('cpu')


x = torch.randn(2, 2)

test_inputs = [x]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (2x12 and 4x9)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., size=(2, 12)), Parameter(FakeTensor(..., size=(9, 4), requires_grad=True)), Parameter(FakeTensor(..., size=(9,), requires_grad=True))), **{}):
a and b must have same reduction dim, but got [2, 12] X [4, 9].

from user code:
   File "<string>", line 24, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/linear.py", line 125, in forward
    return F.linear(input, self.weight, self.bias)


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''