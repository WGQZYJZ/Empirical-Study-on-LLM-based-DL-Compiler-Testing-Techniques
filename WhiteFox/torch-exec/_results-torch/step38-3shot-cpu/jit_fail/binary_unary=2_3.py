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
        super(Model, self).__init__()
        self.conv = torch.nn.Conv2d(3, 32, 1)

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 - 15
        v3 = F.relu(v2)
        v4 = v3 - self.conv(x1)
        v5 = F.relu(v4)
        v6 = self.conv(v1 - 5)
        v7 = v6 - v2
        v8 = self.conv(v7)
        v9 = F.relu(v6)
        return v7



func = Model().to('cpu')


x1 = torch.randn(1, 3, 64, 64)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [32, 3, 1, 1], expected input[1, 32, 64, 64] to have 3 channels, but got 32 channels instead

jit:
Failed running call_function <built-in method conv2d of type object at 0x7c95c3f96ec0>(*(FakeTensor(..., size=(1, 32, 64, 64)), Parameter(FakeTensor(..., size=(32, 3, 1, 1), requires_grad=True)), Parameter(FakeTensor(..., size=(32,), requires_grad=True)), (1, 1), (0, 0), (1, 1), 1), **{}):
Given groups=1, weight of size [32, 3, 1, 1], expected input[1, 32, 64, 64] to have 3 channels, but got 32 channels instead

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