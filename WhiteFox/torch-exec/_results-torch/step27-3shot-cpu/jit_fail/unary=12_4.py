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
        self.conv = torch.nn.Conv2d(640, 160, 16, groups=4)

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.sigmoid(v1)
        v3 = v1 * v2
        v4 = self.conv(v3)
        v5 = v4.sigmoid()
        v6 = v3 * v5
        return v6



func = Model().to('cpu')


x1 = torch.randn(1, 640, 64, 64)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given groups=4, weight of size [160, 160, 16, 16], expected input[1, 160, 49, 49] to have 640 channels, but got 160 channels instead

jit:
Failed running call_function <built-in method conv2d of type object at 0x7a768a396ec0>(*(FakeTensor(..., size=(1, 160, 49, 49)), Parameter(FakeTensor(..., size=(160, 160, 16, 16), requires_grad=True)), Parameter(FakeTensor(..., size=(160,), requires_grad=True)), (1, 1), (0, 0), (1, 1), 4), **{}):
Given groups=4, weight of size [160, 160, 16, 16], expected input[1, 160, 49, 49] to have 640 channels, but got 160 channels instead

from user code:
   File "<string>", line 23, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 554, in forward
    return self._conv_forward(input, self.weight, self.bias)
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 549, in _conv_forward
    return F.conv2d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''