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
        self.conv1 = torch.nn.Conv2d(4, 10, 6, stride=1, padding=1, dilation=2)
        self.conv2 = torch.nn.Conv2d(10, 15, 5, stride=2, padding=1, dilation=2)
        self.conv3 = torch.nn.Conv2d(15, 15, 6, padding=1, dilation=1, groups=15)

    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = self.conv2(v1)
        v3 = self.conv3(v1)
        v4 = v2 + v3
        v5 = v1 + v4
        v6 = v5 * 0.5
        v7 = v5 * v5
        v8 = v7 * v5
        v9 = v8 * 0.044715
        v10 = v5 + v9
        v11 = v10 * 0.7978845608028654
        v12 = torch.tanh(v11)
        v13 = v12 + 1
        v14 = v6 * v13
        return v14



func = Model().to('cpu')


x1 = torch.randn(1, 4, 25, 25)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given groups=15, weight of size [15, 1, 6, 6], expected input[1, 10, 17, 17] to have 15 channels, but got 10 channels instead

jit:
Failed running call_function <built-in method conv2d of type object at 0x766e43796ec0>(*(FakeTensor(..., size=(1, 10, 17, 17)), Parameter(FakeTensor(..., size=(15, 1, 6, 6), requires_grad=True)), Parameter(FakeTensor(..., size=(15,), requires_grad=True)), (1, 1), (1, 1), (1, 1), 15), **{}):
Given groups=15, weight of size [15, 1, 6, 6], expected input[1, 10, 17, 17] to have 15 channels, but got 10 channels instead

from user code:
   File "<string>", line 24, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 554, in forward
    return self._conv_forward(input, self.weight, self.bias)
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 549, in _conv_forward
    return F.conv2d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''