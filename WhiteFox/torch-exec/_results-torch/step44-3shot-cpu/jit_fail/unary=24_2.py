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
        self.conv1 = torch.nn.Conv2d(1, 142, 4, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(142, 12, 3, stride=(2, 2), padding=1)
        self.conv3 = torch.nn.Conv2d(12, 5, 3, stride=1, padding=1)
        self.conv4 = torch.nn.Conv2d(5, 0, 3, stride=1, padding=2)

    def forward(self, x):
        negative_slope = 0.28507218
        v1 = self.conv1(x)
        v2 = v1 > 0
        v3 = v1 * negative_slope
        v4 = torch.where(v2, v1, v3)
        v5 = self.conv2(v4)
        v6 = v5 > 0
        v7 = v5 * negative_slope
        v8 = torch.where(v6, v5, v7)
        v9 = self.conv3(v8)
        v10 = v9 > 0
        v11 = v9 * negative_slope
        v12 = torch.where(v10, v9, v11)
        v13 = self.conv4(v12)
        v14 = v13 > 0
        v15 = v13 * negative_slope
        v16 = torch.where(v14, v13, v15)
        return v16



func = Model().to('cpu')


x1 = torch.randn(5, 64, 64)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [142, 1, 4, 4], expected input[1, 5, 64, 64] to have 1 channels, but got 5 channels instead

jit:
Failed running call_function <built-in method conv2d of type object at 0x71ac1f796ec0>(*(FakeTensor(..., size=(5, 64, 64)), Parameter(FakeTensor(..., size=(142, 1, 4, 4), requires_grad=True)), Parameter(FakeTensor(..., size=(142,), requires_grad=True)), (1, 1), (1, 1), (1, 1), 1), **{}):
Given groups=1, weight of size [142, 1, 4, 4], expected input[1, 5, 64, 64] to have 1 channels, but got 5 channels instead

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