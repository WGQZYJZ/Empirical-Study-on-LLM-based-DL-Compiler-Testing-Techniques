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
        self.conv1 = torch.nn.Conv2d(12, 24, 4, stride=4, padding=0)
        self.conv2 = torch.nn.Conv2d(24, 12, 5)
        self.conv2.bias.data = self.conv1.bias.data

    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = self.conv2(v1)
        v3 = v1 - 0.5
        v4 = v2 - v3
        v5 = F.gelu(v4)
        v6 = v5 - v4
        return v6



func = Model().to('cpu')


x1 = torch.randn(1, 12, 32, 32)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given weight of size [12, 24, 5, 5], expected bias to be 1-dimensional with 12 elements, but got bias of size [24] instead

jit:
Failed running call_function <built-in method conv2d of type object at 0x7c95c3f96ec0>(*(FakeTensor(..., size=(1, 24, (s1//4), (s2//4))), Parameter(FakeTensor(..., size=(12, 24, 5, 5), requires_grad=True)), Parameter(FakeTensor(..., size=(24,), requires_grad=True)), (1, 1), (0, 0), (1, 1), 1), **{}):
Given weight of size [12, 24, 5, 5], expected bias to be 1-dimensional with 12 elements, but got bias of size [24] instead

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