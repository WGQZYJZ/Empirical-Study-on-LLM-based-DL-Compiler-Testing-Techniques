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
        self.conv = torch.nn.Conv2d(1, 8, 1, stride=1)

    def forward(self, x1):
        v1 = torch.relu(self.conv(x1))
        v2 = torch.relu(self.conv(v1))
        v3 = torch.relu(self.conv(v2))
        v4 = torch.relu(self.conv(v3))
        v5 = torch.relu(self.conv(v4))
        v6 = torch.relu(self.conv(v5))
        v7 = torch.relu(self.conv(v6))
        v9 = v7 + self.conv(x1)
        return torch.relu(v9)



func = Model().to('cuda')


x1 = torch.randn(1, 1, 28, 28)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [8, 1, 1, 1], expected input[1, 8, 28, 28] to have 1 channels, but got 8 channels instead

jit:
Failed running call_function <built-in method conv2d of type object at 0x7c3133396ec0>(*(FakeTensor(..., device='cuda:0', size=(1, 8, s0, s1)), Parameter(FakeTensor(..., device='cuda:0', size=(8, 1, 1, 1), requires_grad=True)), Parameter(FakeTensor(..., device='cuda:0', size=(8,), requires_grad=True)), (1, 1), (0, 0), (1, 1), 1), **{}):
Given groups=1, weight of size [8, 1, 1, 1], expected input[1, 8, s0, s1] to have 1 channels, but got 8 channels instead

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