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
        self.linear = torch.nn.Linear(2, 2)
        self.conv = torch.nn.Conv2d(2, 2, 1)

    def forward(self, x1):
        v1 = x1.permute(0, 2, 1)
        v2 = torch.nn.functional.linear(v1, self.linear.weight, self.linear.bias)
        v3 = v2 + 1
        v4 = torch.nn.functional.relu(v3)
        v5 = self.conv(v4)
        v6 = v5
        return v5 - v6



func = Model().to('cpu')


x1 = torch.randn(1, 2, 2)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [2, 2, 1, 1], expected input[1, 1, 2, 2] to have 2 channels, but got 1 channels instead

jit:
Failed running call_function <built-in method conv2d of type object at 0x73dbbe996ec0>(*(FakeTensor(..., size=(1, s1, 2)), Parameter(FakeTensor(..., size=(2, 2, 1, 1), requires_grad=True)), Parameter(FakeTensor(..., size=(2,), requires_grad=True)), (1, 1), (0, 0), (1, 1), 1), **{}):
Given groups=1, weight of size [2, 2, 1, 1], expected input[1, 1, s1, 2] to have 2 channels, but got 1 channels instead

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