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
        self.conv1 = torch.nn.Conv2d(1, 3040, 1, stride=1, padding=0)
        self.conv2 = torch.nn.Conv2d(3040, 384, 1, stride=1, padding=0)
        self.conv3 = torch.nn.Conv2d(9, 153, 3, stride=2, padding=1)
        self.conv4 = torch.nn.Conv2d(153, 32, 1, stride=1, padding=0)
        self.conv5 = torch.nn.Conv2d(1, 1, 1, stride=1, padding=0)
        self.conv6 = torch.nn.Conv2d(13, 1, 1, stride=1, padding=0)

    def forward(self, x1):
        v1 = self.conv1(x1)
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
        v13 = self.conv3(x1)
        v14 = self.conv4(v13)
        v15 = self.conv5(x1)
        v16 = self.conv6(x1)
        v17 = v14 + v15 + v16
        return v17



func = Model().to('cpu')


x1 = torch.randn(1, 9, 397, 37)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [3040, 1, 1, 1], expected input[1, 9, 397, 37] to have 1 channels, but got 9 channels instead

jit:
Failed running call_function <built-in method conv2d of type object at 0x72d07fd96ec0>(*(FakeTensor(..., size=(1, 9, 397, 37)), Parameter(FakeTensor(..., size=(3040, 1, 1, 1), requires_grad=True)), Parameter(FakeTensor(..., size=(3040,), requires_grad=True)), (1, 1), (0, 0), (1, 1), 1), **{}):
Given groups=1, weight of size [3040, 1, 1, 1], expected input[1, 9, 397, 37] to have 1 channels, but got 9 channels instead

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