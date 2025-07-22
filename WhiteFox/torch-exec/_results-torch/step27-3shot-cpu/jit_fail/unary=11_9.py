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
        self.bn = torch.nn.BatchNorm2d(16)
        self.conv_transpose = torch.nn.ConvTranspose2d(16, 8, 3, stride=2, padding=0)

    def forward(self, x1):
        v1 = self.conv_transpose(x1)
        v2 = v1 + 3
        v3 = torch.clamp_min(v2, 0)
        v4 = torch.clamp_max(v3, 6)
        v5 = v4 / 6
        return self.bn(v5)



func = Model().to('cpu')


x1 = torch.randn(1, 16, 128, 128)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
running_mean should contain 8 elements not 16

jit:
Failed running call_function <function batch_norm at 0x735add32ae50>(*(FakeTensor(..., size=(1, 8, 2*s1 + 1, 2*s2 + 1)), FakeTensor(..., size=(16,)), FakeTensor(..., size=(16,)), Parameter(FakeTensor(..., size=(16,), requires_grad=True)), Parameter(FakeTensor(..., size=(16,), requires_grad=True)), False, 0.1, 1e-05), **{}):
running_mean should contain 8 elements not 16

from user code:
   File "<string>", line 26, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/batchnorm.py", line 193, in forward
    return F.batch_norm(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''