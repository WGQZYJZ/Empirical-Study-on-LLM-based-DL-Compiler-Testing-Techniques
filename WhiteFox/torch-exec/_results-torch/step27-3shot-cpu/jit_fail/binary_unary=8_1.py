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
        self.conv1 = torch.nn.Conv2d(3, 8, 3, stride=1, padding=1)
        self.conv3 = torch.nn.Conv2d(8, 16, 3, stride=1, padding=1)
        self.conv5 = torch.nn.Conv2d(16, 32, 3, stride=1, padding=1)
        self.conv6 = torch.nn.Conv2d(32, 32, 3, stride=1, padding=3)

    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = self.conv1(x1)
        v3 = self.conv5(x1)
        v4 = self.conv5(x1)
        v5 = torch.cat([v1, v2, v3, v4], axis=1)
        v6 = self.conv6(v5)
        v7 = torch.sigmoid(v6)
        return v7



func = Model().to('cpu')


x1 = torch.randn(1, 3, 224, 224)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [32, 16, 3, 3], expected input[1, 3, 224, 224] to have 16 channels, but got 3 channels instead

jit:
Failed running call_function <built-in method conv2d of type object at 0x741208d96ec0>(*(FakeTensor(..., size=(1, 3, 224, 224)), Parameter(FakeTensor(..., size=(32, 16, 3, 3), requires_grad=True)), Parameter(FakeTensor(..., size=(32,), requires_grad=True)), (1, 1), (1, 1), (1, 1), 1), **{}):
Given groups=1, weight of size [32, 16, 3, 3], expected input[1, 3, 224, 224] to have 16 channels, but got 3 channels instead

from user code:
   File "<string>", line 25, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 554, in forward
    return self._conv_forward(input, self.weight, self.bias)
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 549, in _conv_forward
    return F.conv2d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''