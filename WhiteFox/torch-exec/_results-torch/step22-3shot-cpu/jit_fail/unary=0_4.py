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
        self.conv1 = torch.nn.Conv2d(32, 32, 2, stride=1, padding=0)
        self.conv2 = torch.nn.Conv2d(32, 128, 3, stride=1, padding=0)
        self.conv3 = torch.nn.Conv2d(1, 128, 9, stride=1, padding=0)

    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = self.conv2(v1)
        v3 = self.conv3(x1)
        v4 = v2 + v3
        v5 = v4 * 0.5
        v6 = v4 * v4
        v7 = v6 * v4
        v8 = v7 * 0.044715
        v9 = v4 + v8
        v10 = v9 * 0.7978845608028654
        v11 = torch.tanh(v10)
        v12 = v11 + 1
        v13 = v5 * v12
        return v13



func = Model().to('cpu')


x1 = torch.randn(1, 32, 32, 32)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [128, 1, 9, 9], expected input[1, 32, 32, 32] to have 1 channels, but got 32 channels instead

jit:
Failed running call_function <built-in method conv2d of type object at 0x753c09996ec0>(*(FakeTensor(..., size=(1, 32, 32, 32)), Parameter(FakeTensor(..., size=(128, 1, 9, 9), requires_grad=True)), Parameter(FakeTensor(..., size=(128,), requires_grad=True)), (1, 1), (0, 0), (1, 1), 1), **{}):
Given groups=1, weight of size [128, 1, 9, 9], expected input[1, 32, 32, 32] to have 1 channels, but got 32 channels instead

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