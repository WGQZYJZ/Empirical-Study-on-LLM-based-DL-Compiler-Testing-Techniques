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
        self.conv = torch.nn.Conv2d(12, 13, 2, stride=2)
        self.conv2 = torch.nn.Conv2d(11, 14, 1, stride=1, padding=1)

    def forward(self, x):
        x = self.conv(x)
        x = torch.tanh(x)
        return self.conv2(x)



func = Model().to('cuda')


x = torch.randn(1, 12, 32, 32)

test_inputs = [x]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [14, 11, 1, 1], expected input[1, 13, 16, 16] to have 11 channels, but got 13 channels instead

jit:
Failed running call_function <built-in method conv2d of type object at 0x73e0e2396ec0>(*(FakeTensor(..., device='cuda:0', size=(1, 13, (s1//2), (s2//2))), Parameter(FakeTensor(..., device='cuda:0', size=(14, 11, 1, 1), requires_grad=True)), Parameter(FakeTensor(..., device='cuda:0', size=(14,), requires_grad=True)), (1, 1), (1, 1), (1, 1), 1), **{}):
Given groups=1, weight of size [14, 11, 1, 1], expected input[1, 13, (s1//2), (s2//2)] to have 11 channels, but got 13 channels instead

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