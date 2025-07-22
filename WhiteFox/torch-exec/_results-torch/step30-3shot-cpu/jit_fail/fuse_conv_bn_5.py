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
        self.conv1 = torch.nn.Conv2d(20, 10, 5)
        self.conv2 = torch.nn.Conv2d(10, 5, 3)
        self.conv3 = torch.nn.Conv2d(5, 30, 1)
        self.bn1 = torch.nn.BatchNorm2d(20)
        self.bn2 = torch.nn.BatchNorm2d(10)
        self.bn3 = torch.nn.BatchNorm2d(5)

    def forward(self, x1):
        y1 = self.conv1(x1)
        y2 = self.conv2(y1)
        y3 = self.conv3(y2)
        y4 = self.bn1(x1)
        y5 = self.bn2(y4)
        y6 = self.bn3(y5)
        y7 = y3 + y6
        return y7



func = Model().to('cpu')


x2 = torch.randn(1, 20, 28, 28)

test_inputs = [x2]

# JIT_FAIL
'''
direct:
running_mean should contain 20 elements not 10

jit:
Failed running call_function <function batch_norm at 0x7e5083bebe50>(*(FakeTensor(..., size=(1, 20, s1, s2)), FakeTensor(..., size=(10,)), FakeTensor(..., size=(10,)), Parameter(FakeTensor(..., size=(10,), requires_grad=True)), Parameter(FakeTensor(..., size=(10,), requires_grad=True)), False, 0.1, 1e-05), **{}):
running_mean should contain 20 elements not 10

from user code:
   File "<string>", line 29, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/batchnorm.py", line 193, in forward
    return F.batch_norm(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''