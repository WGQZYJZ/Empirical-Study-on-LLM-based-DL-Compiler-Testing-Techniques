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
        self.conv = torch.nn.Conv2d(2, 1, 3, 1, 0)
        self.bn = torch.nn.BatchNorm2d(2)

    def forward(self, x):
        return torch.nn.ReLU(self.bn(self.conv(x)) + self.bn(self.conv(x)))



func = Model().to('cpu')


x = torch.randn(1, 2, 6, 6)

test_inputs = [x]

# JIT_FAIL
'''
direct:
running_mean should contain 1 elements not 2

jit:
Failed running call_function <function batch_norm at 0x7a93c00aae50>(*(FakeTensor(..., size=(1, 1, 4, 4)), FakeTensor(..., size=(2,)), FakeTensor(..., size=(2,)), Parameter(FakeTensor(..., size=(2,), requires_grad=True)), Parameter(FakeTensor(..., size=(2,), requires_grad=True)), False, 0.1, 1e-05), **{}):
running_mean should contain 1 elements not 2

from user code:
   File "<string>", line 21, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/batchnorm.py", line 193, in forward
    return F.batch_norm(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''