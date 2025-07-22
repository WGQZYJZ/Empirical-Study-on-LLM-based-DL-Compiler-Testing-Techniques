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
        self.conv1 = torch.nn.Conv2d(64, 128, kernel_size=3, stride=1, padding=1, bias=False)
        self.batchnorm1 = torch.nn.BatchNorm2d(64)
        self.conv2 = torch.nn.Conv2d(64, 64, kernel_size=3, stride=1, padding=1, bias=False)
        self.batchnorm2 = torch.nn.BatchNorm2d(64)

    def forward(self, x):
        x = self.batchnorm1(self.conv1(x))
        x = self.conv2(x)
        x = self.batchnorm2(x)
        return x



func = Model().to('cpu')


x = torch.randn(1, 64, 10, 10)

test_inputs = [x]

# JIT_FAIL
'''
direct:
running_mean should contain 128 elements not 64

jit:
Failed running call_function <function batch_norm at 0x742b0c1ece50>(*(FakeTensor(..., size=(1, 128, 10, 10)), FakeTensor(..., size=(64,)), FakeTensor(..., size=(64,)), Parameter(FakeTensor(..., size=(64,), requires_grad=True)), Parameter(FakeTensor(..., size=(64,), requires_grad=True)), False, 0.1, 1e-05), **{}):
running_mean should contain 128 elements not 64

from user code:
   File "<string>", line 23, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/batchnorm.py", line 193, in forward
    return F.batch_norm(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''