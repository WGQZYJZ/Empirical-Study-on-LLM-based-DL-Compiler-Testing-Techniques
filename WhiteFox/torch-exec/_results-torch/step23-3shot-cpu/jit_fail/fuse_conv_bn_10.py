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
        self.relu = torch.nn.ReLU()
        self.conv1 = torch.nn.Conv1d(2, 2, 2)
        self.bn1 = torch.nn.BatchNorm1d(2)
        self.conv2 = torch.nn.Conv1d(2, 2, 2)
        self.bn2 = torch.nn.BatchNorm1d(2)
        self.conv3 = torch.nn.Conv1d(2, 2, 3)
        self.bn3 = torch.nn.BatchNorm1d(2)

    def forward(self, x1):
        x1 = self.relu(self.bn1(self.conv1(x1)))
        x1 = self.relu(self.bn2(self.conv2(x1)))
        x1 = self.relu(self.bn3(self.conv3(x1)))
        return x1



func = Model().to('cpu')


x1 = torch.randn(1, 2, 3)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Calculated padded input size per channel: (1). Kernel size: (3). Kernel size can't be greater than actual input size

jit:
Failed running call_function <built-in method conv1d of type object at 0x7a9411d96ec0>(*(FakeTensor(..., size=(1, 2, 1)), Parameter(FakeTensor(..., size=(2, 2, 3), requires_grad=True)), Parameter(FakeTensor(..., size=(2,), requires_grad=True)), (1,), (0,), (1,), 1), **{}):
Trying to create tensor with negative dimension -1: [1, 2, -1]

from user code:
   File "<string>", line 28, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 375, in forward
    return self._conv_forward(input, self.weight, self.bias)
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 370, in _conv_forward
    return F.conv1d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''