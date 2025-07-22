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
        self.in_d = 256
        self.layer = torch.nn.Conv2d(3, self.in_d - 3, 3)
        self.bn = torch.nn.BatchNorm2d(3, momentum=0.0)

    def forward(self, x):
        v1 = self.layer(x)
        v1 = self.bn(v1)
        (v1, _) = torch.split(v1, (self.in_d - 3, 3), 1)
        return v1 + v1



func = Model().to('cpu')


x = torch.randn(3, 3, 128, 128)

test_inputs = [x]

# JIT_FAIL
'''
direct:
running_mean should contain 253 elements not 3

jit:
Failed running call_function <function batch_norm at 0x70392b32be50>(*(FakeTensor(..., size=(3, 253, 126, 126)), FakeTensor(..., size=(3,)), FakeTensor(..., size=(3,)), Parameter(FakeTensor(..., size=(3,), requires_grad=True)), Parameter(FakeTensor(..., size=(3,), requires_grad=True)), False, 0.0, 1e-05), **{}):
running_mean should contain 253 elements not 3

from user code:
   File "<string>", line 23, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/batchnorm.py", line 193, in forward
    return F.batch_norm(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''