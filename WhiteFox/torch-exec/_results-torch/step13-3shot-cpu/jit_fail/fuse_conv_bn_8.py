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
        self.conv1 = torch.nn.Conv2d(1, 3, 2)
        self.bn = torch.nn.BatchNorm2d(1)
        self.relu = torch.nn.ReLU()
        self.conv2 = torch.nn.Conv2d(1, 3, 2)
        self.sigmoid = torch.nn.Sigmoid()

    def forward(self, x):
        x = self.conv1(x)
        x = self.bn(x)
        x = self.relu(x)
        x = self.conv2(x)
        x = self.sigmoid(x)
        return x



func = Model().to('cpu')


x = torch.randn(1, 1, 4, 4)

test_inputs = [x]

# JIT_FAIL
'''
direct:
running_mean should contain 3 elements not 1

jit:
Failed running call_function <function batch_norm at 0x74a66026be50>(*(FakeTensor(..., size=(1, 3, 3, 3)), FakeTensor(..., size=(1,)), FakeTensor(..., size=(1,)), Parameter(FakeTensor(..., size=(1,), requires_grad=True)), Parameter(FakeTensor(..., size=(1,), requires_grad=True)), False, 0.1, 1e-05), **{}):
running_mean should contain 3 elements not 1

from user code:
   File "<string>", line 25, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/batchnorm.py", line 193, in forward
    return F.batch_norm(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''