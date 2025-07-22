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
        self.conv_t = torch.nn.ConvTranspose2d(3, 12, 1, stride=1, padding=0, bias=False)
        self.fc = torch.nn.Linear(12, 1)

    def forward(self, x):
        x1 = self.conv_t(x)
        x2 = self.fc(x1.flatten(1))
        return x2



func = Model().to('cpu')


x = torch.randn(2, 3, 10, 20)

test_inputs = [x]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (2x2400 and 12x1)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., size=(2, 2400)), Parameter(FakeTensor(..., size=(1, 12), requires_grad=True)), Parameter(FakeTensor(..., size=(1,), requires_grad=True))), **{}):
a and b must have same reduction dim, but got [2, 2400] X [12, 1].

from user code:
   File "<string>", line 22, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/linear.py", line 125, in forward
    return F.linear(input, self.weight, self.bias)


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''