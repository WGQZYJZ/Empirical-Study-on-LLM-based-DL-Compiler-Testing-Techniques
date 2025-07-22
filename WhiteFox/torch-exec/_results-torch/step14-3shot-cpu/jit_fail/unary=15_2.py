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
        self.conv1 = torch.nn.Conv2d(3, 128, 3, stride=1, padding=1)
        self.bn1 = torch.nn.BatchNorm2d(128)
        self.conv2 = torch.nn.Conv2d(128, 128, 3, stride=1, padding=1)
        self.bn2 = torch.nn.BatchNorm2d(128)
        self.conv3 = torch.nn.Conv2d(128, 2, 3, stride=1, padding=1)

    def forward(self, x1):
        v1 = self.bn2(self.conv3(self.bn1(self.conv2(self.conv1(x1)))))
        return v1



func = Model().to('cpu')


x1 = torch.randn(1, 3, 300, 300)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
running_mean should contain 2 elements not 128

jit:
Failed running call_function <function batch_norm at 0x7da0d3aade50>(*(FakeTensor(..., size=(1, 2, 300, 300)), FakeTensor(..., size=(128,)), FakeTensor(..., size=(128,)), Parameter(FakeTensor(..., size=(128,), requires_grad=True)), Parameter(FakeTensor(..., size=(128,), requires_grad=True)), False, 0.1, 1e-05), **{}):
running_mean should contain 2 elements not 128

from user code:
   File "<string>", line 24, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/batchnorm.py", line 193, in forward
    return F.batch_norm(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''