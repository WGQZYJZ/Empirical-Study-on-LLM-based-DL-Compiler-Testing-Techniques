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

class ModelTanh(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.layer = torch.nn.modules.ModuleList([torch.nn.Linear(20, 30), torch.nn.Tanh(), torch.nn.Linear(30, 40)])
        self.conv = torch.nn.Conv2d(20, 40, kernel_size=1, padding=0)
        self.sigmoid = torch.nn.Sigmoid()

    def forward(self, x):
        for i in range(0, 3):
            l = self.layer[i]
            x = l(x)
        conv = self.conv(x)
        tanh = torch.tanh(conv)
        return tanh



func = ModelTanh().to('cpu')


x = torch.randn(1, 20, 1, 1)

test_inputs = [x]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (20x1 and 20x30)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., size=(1, 20, 1, 1)), Parameter(FakeTensor(..., size=(30, 20), requires_grad=True)), Parameter(FakeTensor(..., size=(30,), requires_grad=True))), **{}):
a and b must have same reduction dim, but got [20, 1] X [20, 30].

from user code:
   File "<string>", line 24, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/linear.py", line 125, in forward
    return F.linear(input, self.weight, self.bias)


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''