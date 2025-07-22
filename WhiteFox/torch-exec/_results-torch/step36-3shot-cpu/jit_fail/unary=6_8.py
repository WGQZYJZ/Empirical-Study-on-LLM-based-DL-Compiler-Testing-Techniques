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
        self.conv = torch.nn.Conv2d(3, 3, 1, stride=1, padding=1, groups=3)
        self.bn = torch.nn.BatchNorm2d(6)

    def forward(self, x1):
        v1 = torch.ceil(self.conv(x1))
        v2 = torch.exp(v1 * 3)
        v3 = torch.clamp_min(v2, 0)
        v4 = torch.clamp_max(v3, 6)
        v5 = v1 * v4
        v6 = v5 / 6
        v7 = self.bn(v6)
        return v7



func = Model().to('cpu')


x1 = torch.randn(1, 3, 256, 256)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
running_mean should contain 3 elements not 6

jit:
Failed running call_function <function batch_norm at 0x749729eebe50>(*(FakeTensor(..., size=(1, 3, 258, 258)), FakeTensor(..., size=(6,)), FakeTensor(..., size=(6,)), Parameter(FakeTensor(..., size=(6,), requires_grad=True)), Parameter(FakeTensor(..., size=(6,), requires_grad=True)), False, 0.1, 1e-05), **{}):
running_mean should contain 3 elements not 6

from user code:
   File "<string>", line 27, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/batchnorm.py", line 193, in forward
    return F.batch_norm(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''