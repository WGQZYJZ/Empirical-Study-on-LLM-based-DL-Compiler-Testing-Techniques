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

class ModelTanh(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 1, kernel_size=5, padding=5, bias=False)
        self.conv2 = torch.nn.Conv2d(1, 3, kernel_size=5, padding=5, bias=False)
        self.bn1 = torch.nn.BatchNorm2d(1)
        self.bn2 = torch.nn.BatchNorm2d(3)

    def forward(self, x):
        v1 = self.bn1(x)
        v2 = self.conv1(v1)
        v3 = torch.tanh(v2)
        v4 = self.bn2(v3)
        v5 = self.conv2(v4)
        return torch.tanh(v5)



func = ModelTanh().to('cpu')


x = torch.randn(1, 3, 224, 224)

test_inputs = [x]

# JIT_FAIL
'''
direct:
running_mean should contain 3 elements not 1

jit:
Failed running call_function <function batch_norm at 0x7de90eb2ae50>(*(FakeTensor(..., size=(1, 3, 224, 224)), FakeTensor(..., size=(1,)), FakeTensor(..., size=(1,)), Parameter(FakeTensor(..., size=(1,), requires_grad=True)), Parameter(FakeTensor(..., size=(1,), requires_grad=True)), False, 0.1, 1e-05), **{}):
running_mean should contain 3 elements not 1

from user code:
   File "<string>", line 23, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/batchnorm.py", line 193, in forward
    return F.batch_norm(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''