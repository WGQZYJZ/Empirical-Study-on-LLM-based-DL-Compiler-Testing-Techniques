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
        self.conv = torch.nn.Conv2d(1, 16, 1, stride=1, padding=1)
        self.linear = torch.nn.Linear(576, 128)

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.flatten(v1, start_dim=1)
        v3 = self.linear(v2)
        v4 = torch.clamp(v3 + 3, 0, 6)
        v5 = v4 / 6
        return v5


func = Model().to('cpu')


x1 = torch.randn(1, 1, 64, 64)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (1x69696 and 576x128)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., size=(1, 69696)), Parameter(FakeTensor(..., size=(128, 576), requires_grad=True)), Parameter(FakeTensor(..., size=(128,), requires_grad=True))), **{}):
a and b must have same reduction dim, but got [1, 69696] X [576, 128].

from user code:
   File "<string>", line 23, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/linear.py", line 125, in forward
    return F.linear(input, self.weight, self.bias)


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''