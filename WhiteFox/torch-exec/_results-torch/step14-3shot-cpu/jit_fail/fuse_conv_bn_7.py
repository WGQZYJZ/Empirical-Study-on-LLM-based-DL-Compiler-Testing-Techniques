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
        self.conv1 = torch.nn.Conv2d(1, 1, 4)
        self.conv2 = torch.nn.Conv2d(1, 1, 2)
        self.conv3 = torch.nn.Conv2d(1, 1, 1)

    def forward(self, x):
        t1 = self.conv1(x)
        t2 = self.conv2(t1) if t1 is not None else None
        t7 = self.conv3(t2) if t2 is not None else None
        return t7



func = Model().to('cpu')


x = torch.randn(1, 3, 3, 3)

test_inputs = [x]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [1, 1, 4, 4], expected input[1, 3, 3, 3] to have 1 channels, but got 3 channels instead

jit:
Failed running call_function <built-in method conv2d of type object at 0x78f363d96ec0>(*(FakeTensor(..., size=(1, 3, 3, 3)), Parameter(FakeTensor(..., size=(1, 1, 4, 4), requires_grad=True)), Parameter(FakeTensor(..., size=(1,), requires_grad=True)), (1, 1), (0, 0), (1, 1), 1), **{}):
Given groups=1, weight of size [1, 1, 4, 4], expected input[1, 3, 3, 3] to have 1 channels, but got 3 channels instead

from user code:
   File "<string>", line 22, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 554, in forward
    return self._conv_forward(input, self.weight, self.bias)
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 549, in _conv_forward
    return F.conv2d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''