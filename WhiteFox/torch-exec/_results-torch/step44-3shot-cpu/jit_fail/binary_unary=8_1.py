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
        self.conv1 = torch.nn.Conv2d(16, 32, 3, stride=2, groups=16)

    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = torch.relu(v1)
        v3 = v2 + v2
        v4 = v3 + v3
        v5 = v2 + v4
        v6 = v2 + v3 + v4 + v2 + v3 + v4 + v5 + v5
        v7 = torch.relu(v6)
        v8 = self.conv1(v7)
        v9 = self.conv1(v8)
        v10 = self.conv1(v9)
        v11 = torch.relu(v10)
        v12 = v7 + v8 + v9
        v13 = v10 + v11
        v14 = v11 + v10
        v15 = torch.relu(v13)
        w5 = v12 + v13
        w6 = v14 + v13 + v13
        w7 = v13 + v15
        w8 = v14 + v15
        w9 = v12 + v14
        torch.cat([w5 + w6, w7, w8, w9], axis=1)
        return w5



func = Model().to('cpu')


x1 = torch.randn(1, 16, 28, 32)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given groups=16, weight of size [32, 1, 3, 3], expected input[1, 32, 13, 15] to have 16 channels, but got 32 channels instead

jit:
Failed running call_function <built-in method conv2d of type object at 0x76c699396ec0>(*(FakeTensor(..., size=(1, 32, 13, 15)), Parameter(FakeTensor(..., size=(32, 1, 3, 3), requires_grad=True)), Parameter(FakeTensor(..., size=(32,), requires_grad=True)), (2, 2), (0, 0), (1, 1), 16), **{}):
Given groups=16, weight of size [32, 1, 3, 3], expected input[1, 32, 13, 15] to have 16 channels, but got 32 channels instead

from user code:
   File "<string>", line 27, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 554, in forward
    return self._conv_forward(input, self.weight, self.bias)
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 549, in _conv_forward
    return F.conv2d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''