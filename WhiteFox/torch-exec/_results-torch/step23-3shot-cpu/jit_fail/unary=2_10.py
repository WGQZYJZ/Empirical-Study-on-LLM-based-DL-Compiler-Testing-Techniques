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
        self.bn = torch.nn.BatchNorm2d(8)
        self.conv = torch.nn.ConvTranspose2d(5, 8, 2, stride=1, padding=1)

    def forward(self, x1):
        v1 = self.bn(x1)
        v2 = self.conv(v1)
        v3 = v2 * 0.5
        v4 = v2 * v2 * v2
        v5 = v4 * 0.044715
        v6 = v2 + v5
        v7 = v6 * 0.7978845608028654
        v8 = torch.tanh(v7)
        v9 = v8 + 1
        v10 = v3 * v9
        return v10



func = Model().to('cpu')


x1 = torch.randn(3, 5, 4, 4)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
running_mean should contain 5 elements not 8

jit:
Failed running call_function <function batch_norm at 0x7749c6669e50>(*(FakeTensor(..., size=(3, 5, 4, 4)), FakeTensor(..., size=(8,)), FakeTensor(..., size=(8,)), Parameter(FakeTensor(..., size=(8,), requires_grad=True)), Parameter(FakeTensor(..., size=(8,), requires_grad=True)), False, 0.1, 1e-05), **{}):
running_mean should contain 5 elements not 8

from user code:
   File "<string>", line 21, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/batchnorm.py", line 193, in forward
    return F.batch_norm(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''