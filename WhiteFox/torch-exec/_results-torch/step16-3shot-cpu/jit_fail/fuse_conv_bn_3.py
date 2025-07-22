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
        self.conv = torch.nn.Conv3d(3, 7, 3)
        self.bn = torch.nn.BatchNorm3d(3, affine=True)

    def forward(self, x1):
        s = self.conv(x1)
        t = self.bn(s)
        return s * t



func = Model().to('cpu')


x1 = torch.randn(1, 3, 4, 4, 4)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
running_mean should contain 7 elements not 3

jit:
Failed running call_function <function batch_norm at 0x7b9fc426ae50>(*(FakeTensor(..., size=(1, 7, s1 - 2, s2 - 2, s3 - 2)), FakeTensor(..., size=(3,)), FakeTensor(..., size=(3,)), Parameter(FakeTensor(..., size=(3,), requires_grad=True)), Parameter(FakeTensor(..., size=(3,), requires_grad=True)), False, 0.1, 1e-05), **{}):
running_mean should contain 7 elements not 3

from user code:
   File "<string>", line 22, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/batchnorm.py", line 193, in forward
    return F.batch_norm(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''