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
        self.conv = torch.nn.Conv2d(3, 3, 1, stride=0, padding=0, dilation=0, groups=1, bias=True)
        self.relu = torch.nn.ReLU()
        self.conv_2 = torch.nn.Conv2d(3, 3, 1, stride=1, padding=0, dilation=1, groups=3, bias=True)

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = self.relu(v1)
        v3 = self.conv_2(v2)
        return v3



func = Model().to('cpu')


x1 = torch.randn(1, 3, 2, 2)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
non-positive stride is not supported

jit:
Failed running call_function <built-in method conv2d of type object at 0x743386d96ec0>(*(FakeTensor(..., size=(1, 3, 2, 2)), Parameter(FakeTensor(..., size=(3, 3, 1, 1), requires_grad=True)), Parameter(FakeTensor(..., size=(3,), requires_grad=True)), (0, 0), (0, 0), (0, 0), 1), **{}):
non-positive stride is not supported

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