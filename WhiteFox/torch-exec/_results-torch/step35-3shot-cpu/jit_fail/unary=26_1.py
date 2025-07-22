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
        self.conv_t = torch.nn.ConvTranspose2d(1, 2, 3, stride=2, padding=1, output_padding=1)
        self.bn = torch.nn.BatchNorm2d(1)
        self.relu = torch.nn.ReLU()

    def forward(self, x3):
        x4 = self.conv_t(x3)
        x5 = self.bn(x4)
        x6 = self.relu(x4)
        return x5 + x6 + 1.651 > 0.622



func = Model().to('cpu')


x3 = torch.randn(2, 1, 11, 11)

test_inputs = [x3]

# JIT_FAIL
'''
direct:
running_mean should contain 2 elements not 1

jit:
Failed running call_function <function batch_norm at 0x7f03fb92ae50>(*(FakeTensor(..., size=(2, 2, 22, 22)), FakeTensor(..., size=(1,)), FakeTensor(..., size=(1,)), Parameter(FakeTensor(..., size=(1,), requires_grad=True)), Parameter(FakeTensor(..., size=(1,), requires_grad=True)), False, 0.1, 1e-05), **{}):
running_mean should contain 2 elements not 1

from user code:
   File "<string>", line 23, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/batchnorm.py", line 193, in forward
    return F.batch_norm(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''