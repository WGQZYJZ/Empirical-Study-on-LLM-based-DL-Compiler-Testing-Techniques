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
        self.conv1 = torch.nn.Conv2d(3, 3, 3)
        self.bn = torch.nn.BatchNorm2d(3, affine=False)

    def forward(self, x):
        s = self.conv1(x)
        y = self.bn(s)
        return y



func = Model().to('cpu')


x = torch.randn(1, 512, 32, 32)

test_inputs = [x]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [3, 3, 3, 3], expected input[1, 512, 32, 32] to have 3 channels, but got 512 channels instead

jit:
Failed running call_function <built-in method conv2d of type object at 0x70248a796ec0>(*(FakeTensor(..., size=(1, 512, 32, 32)), Parameter(FakeTensor(..., size=(3, 3, 3, 3), requires_grad=True)), Parameter(FakeTensor(..., size=(3,), requires_grad=True)), (1, 1), (0, 0), (1, 1), 1), **{}):
Given groups=1, weight of size [3, 3, 3, 3], expected input[1, 512, 32, 32] to have 3 channels, but got 512 channels instead

from user code:
   File "<string>", line 21, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 554, in forward
    return self._conv_forward(input, self.weight, self.bias)
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 549, in _conv_forward
    return F.conv2d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''