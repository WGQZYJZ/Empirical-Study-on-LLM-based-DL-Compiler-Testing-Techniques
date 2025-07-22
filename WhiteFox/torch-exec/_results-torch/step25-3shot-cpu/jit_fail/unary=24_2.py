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
        self.conv = torch.nn.Conv2d(4, 1, 3, stride=2, padding=0)

    def forward(self, x):
        v1 = self.conv(x)
        v2 = v1 > 0
        v3 = v1 * -0.92
        v4 = torch.where(v2, v1, v3)
        return v4



func = Model().to('cpu')


x1 = torch.randn(1, 16, 64, 16)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [1, 4, 3, 3], expected input[1, 16, 64, 16] to have 4 channels, but got 16 channels instead

jit:
Failed running call_function <built-in method conv2d of type object at 0x706c43596ec0>(*(FakeTensor(..., size=(1, 16, 64, 16)), Parameter(FakeTensor(..., size=(1, 4, 3, 3), requires_grad=True)), Parameter(FakeTensor(..., size=(1,), requires_grad=True)), (2, 2), (0, 0), (1, 1), 1), **{}):
Given groups=1, weight of size [1, 4, 3, 3], expected input[1, 16, 64, 16] to have 4 channels, but got 16 channels instead

from user code:
   File "<string>", line 20, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 554, in forward
    return self._conv_forward(input, self.weight, self.bias)
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 549, in _conv_forward
    return F.conv2d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''