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
        self.conv1 = torch.nn.Sequential(torch.nn.Conv2d(3, 64, (1, 3), stride=1, padding=0), torch.nn.BatchNorm2d(64), torch.nn.Flatten(), torch.nn.Linear(65536, 13))

    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = torch.relu(v1)
        return v2



func = Model().to('cpu')


x1 = torch.randn(1, 3, 224, 224)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (1x3182592 and 65536x13)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., size=(1, 64*s1*(s2 - 2))), Parameter(FakeTensor(..., size=(13, 65536), requires_grad=True)), Parameter(FakeTensor(..., size=(13,), requires_grad=True))), **{}):
a and b must have same reduction dim, but got [1, 64*s1*(s2 - 2)] X [65536, 13].

from user code:
   File "<string>", line 20, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/container.py", line 250, in forward
    input = module(input)
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/linear.py", line 125, in forward
    return F.linear(input, self.weight, self.bias)


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''