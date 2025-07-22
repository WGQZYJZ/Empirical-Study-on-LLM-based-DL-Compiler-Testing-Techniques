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

class Model(nn.Module):

    def __init__(self):
        super().__init__()
        self.conv1 = nn.Conv2d(230, 400, 1, stride=1, padding=176)
        self.conv2 = nn.Conv2d(400, 1, 1, stride=1, padding=1)
        self.conv3 = nn.Conv2d(220, 380, 1, stride=1, padding=166)
        self.conv4 = nn.Conv2d(470, 200, 1, stride=1, padding=5)
        self.conv5 = nn.Conv2d(900, 500, 1, stride=1, padding=85)
        self.conv6 = nn.Conv2d(1, 1, 1, stride=1, padding=1)

    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = v1 * 0.5
        v3 = v1 * 0.7071067811865476
        v4 = torch.erf(v3)
        v5 = v4 + 1
        v6 = v2 * v5
        v7 = self.conv2(v6)
        v8 = self.conv3(x1)
        v9 = v8 * 0.5
        v10 = v8 * 0.7071067811865476
        v11 = torch.erf(v10)
        v12 = v11 + 1
        v13 = v9 * v12
        v14 = self.conv4(x1)
        v15 = self.conv5(x1)
        v16 = v15 * 0.5
        v17 = v15 * 0.7071067811865476
        v18 = torch.erf(v17)
        v19 = v18 + 1
        v20 = v16 * v19
        v21 = v20 + v13
        v22 = self.conv6(v21)
        return v22



func = Model().to('cpu')


x1 = torch.randn(1, 230, 64, 64)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [380, 220, 1, 1], expected input[1, 230, 64, 64] to have 220 channels, but got 230 channels instead

jit:
Failed running call_function <built-in method conv2d of type object at 0x731db9d96ec0>(*(FakeTensor(..., size=(1, 230, 64, 64)), Parameter(FakeTensor(..., size=(380, 220, 1, 1), requires_grad=True)), Parameter(FakeTensor(..., size=(380,), requires_grad=True)), (1, 1), (166, 166), (1, 1), 1), **{}):
Given groups=1, weight of size [380, 220, 1, 1], expected input[1, 230, 64, 64] to have 220 channels, but got 230 channels instead

from user code:
   File "<string>", line 32, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 554, in forward
    return self._conv_forward(input, self.weight, self.bias)
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 549, in _conv_forward
    return F.conv2d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''