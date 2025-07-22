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
        self.bn1 = torch.nn.BatchNorm2d(num_features=28, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.bn2 = torch.nn.BatchNorm2d(num_features=64, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.bn3 = torch.nn.BatchNorm2d(num_features=128, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.bn4 = torch.nn.BatchNorm2d(num_features=32, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)

    def forward(self, v1):
        v2 = self.bn1(v1)
        v3 = self.bn2(v2)
        v4 = self.bn3(v3)
        v5 = self.bn4(v4)
        return v5



func = Model().to('cpu')


v1 = torch.randn(1, 64, 34, 298)

test_inputs = [v1]

# JIT_FAIL
'''
direct:
running_mean should contain 64 elements not 28

jit:
Failed running call_function <function batch_norm at 0x7954e20a9e50>(*(FakeTensor(..., size=(1, 64, 34, 298)), FakeTensor(..., size=(28,)), FakeTensor(..., size=(28,)), Parameter(FakeTensor(..., size=(28,), requires_grad=True)), Parameter(FakeTensor(..., size=(28,), requires_grad=True)), False, 0.1, 1e-05), **{}):
running_mean should contain 64 elements not 28

from user code:
   File "<string>", line 23, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/batchnorm.py", line 193, in forward
    return F.batch_norm(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''