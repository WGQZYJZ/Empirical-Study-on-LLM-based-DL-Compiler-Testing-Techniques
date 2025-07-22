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
        self.conv1 = torch.nn.Conv2d(3, 2, 3)
        self.conv2 = torch.nn.Conv2d(2, 2, 3)
        self.conv3 = torch.nn.Conv2d(2, 2, 3)
        self.conv4 = torch.nn.Conv2d(2, 2, 3)

    def forward(self, x):
        v1 = self.conv1(x)
        v2 = self.conv2(v1)
        h3 = self.conv3(v1)
        h4 = self.conv4(v2)
        return (v2, h4)



func = Model().to('cpu')


x = torch.randn(1, 3, 6, 6)

test_inputs = [x]

# JIT_FAIL
'''
direct:
Calculated padded input size per channel: (2 x 2). Kernel size: (3 x 3). Kernel size can't be greater than actual input size

jit:
Failed running call_function <built-in method conv2d of type object at 0x7e50d5796ec0>(*(FakeTensor(..., size=(1, 2, 2, 2)), Parameter(FakeTensor(..., size=(2, 2, 3, 3), requires_grad=True)), Parameter(FakeTensor(..., size=(2,), requires_grad=True)), (1, 1), (0, 0), (1, 1), 1), **{}):
Calculated padded input size per channel: (2 x 2). Kernel size: (3 x 3). Kernel size can't be greater than actual input size

from user code:
   File "<string>", line 26, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 554, in forward
    return self._conv_forward(input, self.weight, self.bias)
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 549, in _conv_forward
    return F.conv2d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''