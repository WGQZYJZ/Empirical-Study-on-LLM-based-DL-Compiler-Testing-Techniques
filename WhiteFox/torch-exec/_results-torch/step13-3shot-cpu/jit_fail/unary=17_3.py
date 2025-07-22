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
        self.conv = torch.nn.ConvTranspose2d(16, 32, 3, padding=1, stride=2)
        self.linear = torch.nn.Linear(32, 1)
        self.relu = torch.nn.ReLU6()

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = self.linear(v1)
        v3 = self.relu(v2)
        return v3



func = Model().to('cpu')


x1 = torch.randn(1, 16, 78, 78)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (4960x155 and 32x1)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., size=(1, 32, 155, 155)), Parameter(FakeTensor(..., size=(1, 32), requires_grad=True)), Parameter(FakeTensor(..., size=(1,), requires_grad=True))), **{}):
a and b must have same reduction dim, but got [4960, 155] X [32, 1].

from user code:
   File "<string>", line 23, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/linear.py", line 125, in forward
    return F.linear(input, self.weight, self.bias)


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''