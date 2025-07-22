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
        self.downconvs = torch.nn.Sequential(*[torch.nn.Conv2d(in_channels=3, out_channels=16, kernel_size=3, padding=1), torch.nn.Conv2d(in_channels=16, out_channels=32, kernel_size=3, padding=1), torch.nn.Conv2d(in_channels=32, out_channels=48, kernel_size=3, padding=1)] * 2)

    def forward(self, x1):
        v1 = self.downconvs(x1)
        v2 = torch.nn.Sigmoid()(v1)
        return v2



func = Model().to('cpu')


x1 = torch.randn(1, 3, 224, 224)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [16, 3, 3, 3], expected input[1, 48, 224, 224] to have 3 channels, but got 48 channels instead

jit:
Failed running call_function <built-in method conv2d of type object at 0x7ce903b96ec0>(*(FakeTensor(..., size=(1, 48, 224, 224)), Parameter(FakeTensor(..., size=(16, 3, 3, 3), requires_grad=True)), Parameter(FakeTensor(..., size=(16,), requires_grad=True)), (1, 1), (1, 1), (1, 1), 1), **{}):
Given groups=1, weight of size [16, 3, 3, 3], expected input[1, 48, 224, 224] to have 3 channels, but got 48 channels instead

from user code:
   File "<string>", line 20, in forward
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