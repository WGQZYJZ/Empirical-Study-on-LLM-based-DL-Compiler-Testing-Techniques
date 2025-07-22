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

class Model2(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 3, 3)
        self.bn = torch.nn.BatchNorm2d(2)

    def forward(self, x1):
        x1 = self.conv(x1)
        x1 = self.bn(x1)
        return x1



func = Model2().to('cpu')


x1 = torch.randn(1, 3, 4, 4)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
running_mean should contain 3 elements not 2

jit:
Failed running call_function <function batch_norm at 0x725e2b4ebe50>(*(FakeTensor(..., size=(1, 3, 2, 2)), FakeTensor(..., size=(2,)), FakeTensor(..., size=(2,)), Parameter(FakeTensor(..., size=(2,), requires_grad=True)), Parameter(FakeTensor(..., size=(2,), requires_grad=True)), False, 0.1, 1e-05), **{}):
running_mean should contain 3 elements not 2

from user code:
   File "<string>", line 22, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/batchnorm.py", line 193, in forward
    return F.batch_norm(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''