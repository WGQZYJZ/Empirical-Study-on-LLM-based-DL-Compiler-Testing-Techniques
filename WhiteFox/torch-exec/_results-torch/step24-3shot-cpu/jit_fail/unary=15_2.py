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
        self.bn1 = torch.nn.Conv2d(3, 3, 1, stride=1, padding=0)
        self.bn2 = torch.nn.BatchNorm2d(8)
        self.bn3 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
        self.bn4 = torch.nn.Conv2d(8, 8, 1, stride=1, padding=0)
        self.bn5 = torch.nn.BatchNorm2d(8)
        self.bn6 = torch.nn.Conv2d(8, 8, 1, stride=1, padding=0)
        self.bn7 = torch.nn.Conv2d(8, 8, 1, stride=1, padding=0)
        self.bn8 = torch.nn.Conv2d(8, 8, 1, stride=1, padding=0)

    def forward(self, x1):
        v1 = self.bn1(x1)
        v2 = self.bn2(v1)
        v3 = self.bn3(v2)
        v4 = self.bn4(v3)
        v5 = self.bn5(v4)
        v6 = self.bn6(v5)
        v7 = self.bn7(v6)
        v8 = self.bn8(v7)
        return v8



func = Model().to('cpu')


x1 = torch.randn(1, 3, 480, 640)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
running_mean should contain 3 elements not 8

jit:
Failed running call_function <function batch_norm at 0x7b06ca76be50>(*(FakeTensor(..., size=(1, 3, 480, 640)), FakeTensor(..., size=(8,)), FakeTensor(..., size=(8,)), Parameter(FakeTensor(..., size=(8,), requires_grad=True)), Parameter(FakeTensor(..., size=(8,), requires_grad=True)), False, 0.1, 1e-05), **{}):
running_mean should contain 3 elements not 8

from user code:
   File "<string>", line 28, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/batchnorm.py", line 193, in forward
    return F.batch_norm(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''