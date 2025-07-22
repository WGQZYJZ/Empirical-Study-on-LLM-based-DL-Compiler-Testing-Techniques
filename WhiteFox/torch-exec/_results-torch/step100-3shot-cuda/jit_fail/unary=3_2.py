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
        self.conv = torch.nn.Conv2d(3, 6, 3, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(6, 5, 3, bias=False, stride=1, padding=1)
        self.conv3 = torch.nn.Conv2d(6, 5, 3, bias=False, stride=1, padding=1)

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = self.conv2(x1)
        v3 = self.conv3(v2)
        v4 = v3 + 1
        v5 = self.conv3(v4)
        return v5



func = Model().to('cuda')


x1 = torch.randn(1, 3, 128, 60)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [5, 6, 3, 3], expected input[1, 3, 128, 60] to have 6 channels, but got 3 channels instead

jit:
Failed running call_function <built-in method conv2d of type object at 0x77ecaa396ec0>(*(FakeTensor(..., device='cuda:0', size=(1, 3, 128, 60)), Parameter(FakeTensor(..., device='cuda:0', size=(5, 6, 3, 3), requires_grad=True)), None, (1, 1), (1, 1), (1, 1), 1), **{}):
Given groups=1, weight of size [5, 6, 3, 3], expected input[1, 3, 128, 60] to have 6 channels, but got 3 channels instead

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