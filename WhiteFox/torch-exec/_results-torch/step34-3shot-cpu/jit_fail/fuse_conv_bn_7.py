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
        self.conv1 = torch.nn.Conv2d(3, 4, 2)
        self.conv2 = torch.nn.Conv2d(3, 5, 2)
        self.bn = torch.nn.BatchNorm2d(3)

    def forward(self, x1):
        s = self.conv1(x1)
        t = self.conv2(s)
        y = self.bn(t)
        return y



func = Model().to('cpu')


x1 = torch.rand(1, 3, 6, 6)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [5, 3, 2, 2], expected input[1, 4, 5, 5] to have 3 channels, but got 4 channels instead

jit:
Failed running call_function <built-in method conv2d of type object at 0x70248a796ec0>(*(FakeTensor(..., size=(1, 4, s1 - 1, s2 - 1)), Parameter(FakeTensor(..., size=(5, 3, 2, 2), requires_grad=True)), Parameter(FakeTensor(..., size=(5,), requires_grad=True)), (1, 1), (0, 0), (1, 1), 1), **{}):
Given groups=1, weight of size [5, 3, 2, 2], expected input[1, 4, s1 - 1, s2 - 1] to have 3 channels, but got 4 channels instead

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