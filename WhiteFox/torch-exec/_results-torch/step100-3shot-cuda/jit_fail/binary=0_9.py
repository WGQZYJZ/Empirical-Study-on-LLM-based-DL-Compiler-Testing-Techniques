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
        self.fc = torch.nn.Linear(3, 8, bias=False)
        self.conv = torch.nn.Conv2d(3, 8, 3, padding=1, bias=False)
        self.bn = torch.nn.BatchNorm2d(8)

    def forward(self, x1, x2):
        x1 = self.fc(x1)
        if x2 == None:
            x2 = torch.randn(x1.shape)
        x3 = self.conv(x2)
        x1 = x2 + x3
        x4 = self.bn(x1)
        v1 = x1 + x4
        return v1



func = Model().to('cuda')


x1 = torch.randn(1, 3, 112, 112)

x2 = torch.randn(1, 3, 292, 292)

test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (336x112 and 3x8)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., device='cuda:0', size=(1, 3, 112, 112)), Parameter(FakeTensor(..., device='cuda:0', size=(8, 3), requires_grad=True)), None), **{}):
a and b must have same reduction dim, but got [336, 112] X [3, 8].

from user code:
   File "<string>", line 22, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/linear.py", line 125, in forward
    return F.linear(input, self.weight, self.bias)


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''