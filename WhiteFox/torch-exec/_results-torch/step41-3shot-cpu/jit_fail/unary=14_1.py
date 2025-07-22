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
        self.conv1 = torch.nn.Conv2d(7, 8, 3)
        self.conv_transpose2 = torch.nn.ConvTranspose2d(12, 24, 5, stride=3, padding=2)
        self.conv3 = torch.nn.Conv2d(18, 6, 7)

    def forward(self, x1):
        v1 = self.conv1(x1)
        v3 = self.conv3(v1)
        v2 = self.conv_transpose2(v3)
        v4 = torch.sigmoid(v2)
        v5 = v2 * v4
        return (v5, v1, v3, v2)



func = Model().to('cpu')


x1 = torch.randn(1, 7, 224, 224)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [6, 18, 7, 7], expected input[1, 8, 222, 222] to have 18 channels, but got 8 channels instead

jit:
Failed running call_function <built-in method conv2d of type object at 0x70e5a8d96ec0>(*(FakeTensor(..., size=(1, 8, 222, 222)), Parameter(FakeTensor(..., size=(6, 18, 7, 7), requires_grad=True)), Parameter(FakeTensor(..., size=(6,), requires_grad=True)), (1, 1), (0, 0), (1, 1), 1), **{}):
Given groups=1, weight of size [6, 18, 7, 7], expected input[1, 8, 222, 222] to have 18 channels, but got 8 channels instead

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