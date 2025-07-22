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
        self.conv = torch.nn.Conv2d(2, 8, 5, stride=2, padding=2, dilation=2)
        self.conv2 = torch.nn.Conv2d(8, 3, 3, stride=2, padding=2, dilation=2)
        self.conv3 = torch.nn.Conv2d(3, 2, 3, stride=1, padding=1)

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 + 0.5
        v3 = self.conv3(v2)
        return v3



func = Model().to('cpu')


x1 = torch.randn(1, 2, 41, 41)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [2, 3, 3, 3], expected input[1, 8, 19, 19] to have 3 channels, but got 8 channels instead

jit:
Failed running call_function <built-in method conv2d of type object at 0x7bf57b396ec0>(*(FakeTensor(..., size=(1, 8, (((s1 - 5)//2)) + 1, (((s2 - 5)//2)) + 1)), Parameter(FakeTensor(..., size=(2, 3, 3, 3), requires_grad=True)), Parameter(FakeTensor(..., size=(2,), requires_grad=True)), (1, 1), (1, 1), (1, 1), 1), **{}):
Given groups=1, weight of size [2, 3, 3, 3], expected input[1, 8, (((s1 - 5)//2)) + 1, (((s2 - 5)//2)) + 1] to have 3 channels, but got 8 channels instead

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