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
        self.conv1 = torch.nn.Conv2d(3, 6, 5, stride=1, padding=0)
        self.conv2 = torch.nn.Conv2d(6, 16, 5, stride=1, padding=1)
        self.flatten = torch.nn.Flatten()

    def forward(self, x):
        v1 = self.conv1(x)
        v2 = torch.relu(v1)
        v3 = torch.nn.functional.relu(v1)
        v4 = self.conv2(v1)
        v5 = torch.nn.functional.max_pool2d(v3, 2)
        v6 = self.conv2(v5)
        v7 = torch.nn.functional.max_pool2d(v3, 2)
        v8 = torch.flatten(v6, 1)
        v9 = torch.flatten(v7, 1)
        v10 = torch.add(v8, v9)
        return v10



func = Model().to('cpu')


x = torch.randn(1, 3, 1, 1)

test_inputs = [x]

# JIT_FAIL
'''
direct:
Calculated padded input size per channel: (1 x 1). Kernel size: (5 x 5). Kernel size can't be greater than actual input size

jit:
Failed running call_function <built-in method conv2d of type object at 0x70547f796ec0>(*(FakeTensor(..., size=(1, 3, 1, 1)), Parameter(FakeTensor(..., size=(6, 3, 5, 5), requires_grad=True)), Parameter(FakeTensor(..., size=(6,), requires_grad=True)), (1, 1), (0, 0), (1, 1), 1), **{}):
Calculated padded input size per channel: (1 x 1). Kernel size: (5 x 5). Kernel size can't be greater than actual input size

from user code:
   File "<string>", line 22, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 554, in forward
    return self._conv_forward(input, self.weight, self.bias)
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 549, in _conv_forward
    return F.conv2d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''