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
        self.conv_1 = torch.nn.Conv2d(160, 1, 3)
        self.conv_1.weight = torch.nn.Parameter(torch.nn.init.normal_(torch.Tensor(64, 160, 3, 3), 0.01, 0.1))
        self.conv_1.bias = torch.nn.Parameter(torch.nn.init.uniform_(torch.Tensor(64, 160, 3, 3), 0.01, 0.1))
        self.conv_2 = torch.nn.Conv2d(64, 1, 3)
        self.conv_2.weight = torch.nn.Parameter(torch.nn.init.normal_(torch.Tensor(160, 64, 3, 3), 0.01, 0.1))
        self.conv_2.bias = torch.nn.Parameter(torch.nn.init.uniform_(torch.Tensor(160, 64, 3, 3), 0.01, 0.1))

    def forward(self, x1):
        v1 = self.conv_1(x1)
        v2 = F.sigmoid(v1)
        v3 = v2 * v1
        v3 = v3.sum(dim=1)
        v4 = self.conv_2(v3)
        return v4



func = Model().to('cpu')


x1 = torch.randn(1, 64, 16, 16)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [64, 160, 3, 3], expected input[1, 64, 16, 16] to have 160 channels, but got 64 channels instead

jit:
Failed running call_function <built-in method conv2d of type object at 0x7818d4996ec0>(*(FakeTensor(..., size=(1, 64, 16, 16)), Parameter(FakeTensor(..., size=(64, 160, 3, 3), requires_grad=True)), Parameter(FakeTensor(..., size=(64, 160, 3, 3), requires_grad=True)), (1, 1), (0, 0), (1, 1), 1), **{}):
Given groups=1, weight of size [64, 160, 3, 3], expected input[1, 64, 16, 16] to have 160 channels, but got 64 channels instead

from user code:
   File "<string>", line 25, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 554, in forward
    return self._conv_forward(input, self.weight, self.bias)
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 549, in _conv_forward
    return F.conv2d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''