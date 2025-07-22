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
        self.conv1 = torch.nn.Conv2d(3, 8, 3, stride=2, padding=1)
        self.conv1_2 = torch.nn.Conv2d(8, 8, 1, stride=2, padding=1)
        self.conv1_3 = torch.nn.Conv2d(8, 8, 1, stride=2, groups=8, padding=1)
        self.bn1_4 = torch.nn.BatchNorm2d(16)
        self.conv1_5 = torch.nn.Conv2d(8, 8, 1, stride=2, padding=1)
        self.conv1_6 = torch.nn.Conv2d(8, 16, 3, stride=2, padding=1)
        self.bn1_7 = torch.nn.BatchNorm2d(16)

    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = self.conv1_2(v1)
        v3 = self.conv1_3(v2)
        v4 = self.bn1_4(v3)
        v5 = self.conv1_5(v1)
        v6 = self.conv1_6(v5)
        v7 = self.bn1_7(v6)
        return v7



func = Model().to('cpu')


x1 = torch.randn(1, 3, 32, 32)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
running_mean should contain 8 elements not 16

jit:
Failed running call_function <function batch_norm at 0x7d5abc9ebe50>(*(FakeTensor(..., size=(1, 8, 6, 6)), FakeTensor(..., size=(16,)), FakeTensor(..., size=(16,)), Parameter(FakeTensor(..., size=(16,), requires_grad=True)), Parameter(FakeTensor(..., size=(16,), requires_grad=True)), False, 0.1, 1e-05), **{}):
running_mean should contain 8 elements not 16

from user code:
   File "<string>", line 29, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/batchnorm.py", line 193, in forward
    return F.batch_norm(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''