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
        self.conv = torch.nn.Conv2d(224, 128, 1, stride=2)
        self.maxpool = torch.nn.MaxPool2d(2, stride=2, padding=0)

    def forward(self, t1):
        v1 = self.conv(t1)
        v2 = v1 - torch.transpose(t1, 2, 1)
        v3 = F.relu(v2)
        v4 = v3 - self.maxpool(t1)
        v5 = F.relu(v4)
        return v5



func = Model().to('cpu')


t1 = torch.randn(1, 3, 224, 224)

test_inputs = [t1]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [128, 224, 1, 1], expected input[1, 3, 224, 224] to have 224 channels, but got 3 channels instead

jit:
Failed running call_function <built-in method conv2d of type object at 0x7c95c3f96ec0>(*(FakeTensor(..., size=(1, 3, 224, 224)), Parameter(FakeTensor(..., size=(128, 224, 1, 1), requires_grad=True)), Parameter(FakeTensor(..., size=(128,), requires_grad=True)), (2, 2), (0, 0), (1, 1), 1), **{}):
Given groups=1, weight of size [128, 224, 1, 1], expected input[1, 3, 224, 224] to have 224 channels, but got 3 channels instead

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