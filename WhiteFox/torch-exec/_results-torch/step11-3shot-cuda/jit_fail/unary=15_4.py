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
        _conv = torch.nn.Conv2d(3, 16, 1, stride=1, padding=2, bias=False)
        self.conv = torch.nn.Sequential(_conv, torch.nn.BatchNorm2d(16), torch.nn.ReLU(), _conv, torch.nn.BatchNorm2d(16), torch.nn.ReLU())

    def forward(self, x1):
        v1 = self.conv(x1)
        return v1



func = Model().to('cuda')


x1 = torch.randn(1, 3, 32, 64)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [16, 3, 1, 1], expected input[1, 16, 36, 68] to have 3 channels, but got 16 channels instead

jit:
Failed running call_function <built-in method conv2d of type object at 0x79e7b9396ec0>(*(FakeTensor(..., device='cuda:0', size=(1, 16, 36, 68)), Parameter(FakeTensor(..., device='cuda:0', size=(16, 3, 1, 1), requires_grad=True)), None, (1, 1), (2, 2), (1, 1), 1), **{}):
Given groups=1, weight of size [16, 3, 1, 1], expected input[1, 16, 36, 68] to have 3 channels, but got 16 channels instead

from user code:
   File "<string>", line 21, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/container.py", line 250, in forward
    input = module(input)
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 554, in forward
    return self._conv_forward(input, self.weight, self.bias)
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 549, in _conv_forward
    return F.conv2d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''