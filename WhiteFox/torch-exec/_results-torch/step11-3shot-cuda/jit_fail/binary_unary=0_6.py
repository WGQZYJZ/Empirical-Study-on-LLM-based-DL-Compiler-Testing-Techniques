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
        self.conv = torch.nn.Conv2d(16, 16, 7, stride=1, padding=3)

    def forward(self, x1, x2):
        v1 = self.conv(x1)
        v2 = torch.relu(v1)
        v3 = torch.cat((v2, x2), dim=1)
        v4 = self.conv(v3)
        v5 = torch.relu(v4)
        v6 = torch.cat((v5, v2), dim=1)
        v7 = self.conv(v6)
        v8 = torch.add(v7, v5)
        v9 = torch.relu(v8)
        return v9



func = Model().to('cuda')


x1 = torch.randn(1, 16, 64, 64)

x2 = torch.randn(1, 16, 64, 64)

test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [16, 16, 7, 7], expected input[1, 32, 64, 64] to have 16 channels, but got 32 channels instead

jit:
Failed running call_function <built-in method conv2d of type object at 0x71bf61196ec0>(*(FakeTensor(..., device='cuda:0', size=(1, s0 + 16, 64, 64)), Parameter(FakeTensor(..., device='cuda:0', size=(16, 16, 7, 7), requires_grad=True)), Parameter(FakeTensor(..., device='cuda:0', size=(16,), requires_grad=True)), (1, 1), (3, 3), (1, 1), 1), **{}):
Given groups=1, weight of size [16, 16, 7, 7], expected input[1, s0 + 16, 64, 64] to have 16 channels, but got s0 + 16 channels instead

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