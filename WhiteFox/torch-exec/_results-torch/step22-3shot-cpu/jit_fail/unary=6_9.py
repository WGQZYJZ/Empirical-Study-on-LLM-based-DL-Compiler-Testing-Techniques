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
        self.conv = torch.nn.Conv2d(3, 6, 2, stride=2, padding=4)
        self.fc = torch.nn.Linear(832, 1)

    def forward(self, x1):
        v1 = self.conv(x1)
        v1 = v1.flatten(1)
        v2 = self.fc(v1)
        v3 = v2 + 3
        v4 = torch.relu(v3)
        v5 = v4 * 6
        return v5



func = Model().to('cpu')


x1 = torch.randn(1, 3, 28, 28)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (1x1944 and 832x1)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., size=(1, 1944)), Parameter(FakeTensor(..., size=(1, 832), requires_grad=True)), Parameter(FakeTensor(..., size=(1,), requires_grad=True))), **{}):
a and b must have same reduction dim, but got [1, 1944] X [832, 1].

from user code:
   File "<string>", line 23, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/linear.py", line 125, in forward
    return F.linear(input, self.weight, self.bias)


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''