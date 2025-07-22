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
        self.conv1 = torch.nn.Conv2d(8, 16, kernel_size=3, stride=2, padding=1)
        self.relu1 = torch.nn.LeakyReLU(-0.01)
        self.bn1 = torch.nn.BatchNorm2d(8)

    def forward(self, x):
        v1 = self.conv1(x)
        v2 = self.relu1(v1)
        v3 = self.bn1(v2)
        v4 = v2 > 0
        v5 = v2 * -0.1
        v6 = torch.where(v4, v2, v5)
        return v6



func = Model().to('cpu')


x1 = torch.randn(1, 8, 128, 128)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
running_mean should contain 16 elements not 8

jit:
Failed running call_function <function batch_norm at 0x706bf1969e50>(*(FakeTensor(..., size=(1, 16, 64, 64)), FakeTensor(..., size=(8,)), FakeTensor(..., size=(8,)), Parameter(FakeTensor(..., size=(8,), requires_grad=True)), Parameter(FakeTensor(..., size=(8,), requires_grad=True)), False, 0.1, 1e-05), **{}):
running_mean should contain 16 elements not 8

from user code:
   File "<string>", line 24, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/batchnorm.py", line 193, in forward
    return F.batch_norm(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''