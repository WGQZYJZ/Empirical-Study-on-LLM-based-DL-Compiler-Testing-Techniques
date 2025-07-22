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
        self.conv_t_3 = torch.nn.ConvTranspose2d(3, 112, (1, 4), stride=1, padding=(1, 1), bias=False)
        self.bn = torch.nn.BatchNorm2d(3)

    def forward(self, x):
        y = self.conv_t_3(x)
        y1 = y > 0
        y2 = y * 2.498
        y3 = torch.where(y1, y, y2)
        y4 = self.bn(y3)
        return y4



func = Model().to('cpu')


x = torch.randn(1, 3, 11, 13)

test_inputs = [x]

# JIT_FAIL
'''
direct:
running_mean should contain 112 elements not 3

jit:
Failed running call_function <function batch_norm at 0x7f74f506ae50>(*(FakeTensor(..., size=(1, 112, s1 - 2, s2 + 1)), FakeTensor(..., size=(3,)), FakeTensor(..., size=(3,)), Parameter(FakeTensor(..., size=(3,), requires_grad=True)), Parameter(FakeTensor(..., size=(3,), requires_grad=True)), False, 0.1, 1e-05), **{}):
running_mean should contain 112 elements not 3

from user code:
   File "<string>", line 25, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/batchnorm.py", line 193, in forward
    return F.batch_norm(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''