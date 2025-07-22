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
        self.conv = torch.nn.Conv2d(55, 10, 3, stride=2, padding=2, dilation=1)
        self.conv2 = torch.nn.Conv2d(10, 10, 3, stride=2, padding=1, dilation=2)
        self.conv3 = torch.nn.Conv2d(10, 15, 1, stride=1, padding=0)
        self.conv4 = torch.nn.Conv2d(15, 20, 3, stride=2, padding=2, dilation=3)
        self.conv5 = torch.nn.Conv2d(20, 2, 1, stride=1, padding=0)

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 * 0.5
        v3 = v1 * 0.7071067811865476
        v4 = torch.erf(v3)
        v5 = v4 + 1
        v6 = v2 * v5
        v7 = self.conv2(v6)
        v8 = v7 * 0.5
        v9 = v7 * 0.7071067811865476
        v10 = torch.erf(v9)
        v11 = v10 + 1
        v12 = v8 * v11
        v13 = self.conv3(v12)
        v14 = v13 * 0.5
        v15 = v13 * 0.7071067811865476
        v16 = torch.erf(v15)
        v17 = v16 + 1
        v18 = v14 * v17
        v19 = self.conv4(v18)
        v20 = v19 * 0.5
        v21 = v19 * 0.7071067811865476
        v22 = torch.erf(v21)
        v23 = v22 + 1
        v24 = v20 * v23
        v25 = self.conv5(v24)
        return v25



func = Model().to('cpu')


x1 = torch.randn(1, 55, 12, 10)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Calculated padded input size per channel: (7 x 6). Kernel size: (7 x 7). Kernel size can't be greater than actual input size

jit:
Failed running call_function <built-in method conv2d of type object at 0x738cbc396ec0>(*(FakeTensor(..., size=(1, 15, 3, 2)), Parameter(FakeTensor(..., size=(20, 15, 3, 3), requires_grad=True)), Parameter(FakeTensor(..., size=(20,), requires_grad=True)), (2, 2), (2, 2), (3, 3), 1), **{}):
Calculated padded input size per channel: (7 x 6). Kernel size: (7 x 7). Kernel size can't be greater than actual input size

from user code:
   File "<string>", line 42, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 554, in forward
    return self._conv_forward(input, self.weight, self.bias)
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 549, in _conv_forward
    return F.conv2d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''