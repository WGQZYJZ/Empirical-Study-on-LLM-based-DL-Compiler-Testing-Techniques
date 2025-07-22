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

class ModelTanh(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.model = torch.nn.Sequential(torch.nn.Conv2d(3, 32, 7, stride=2, padding=2, bias=True, dilation=2), torch.nn.BatchNorm2d(32), torch.nn.MaxPool2d(2), torch.nn.ReLU(), torch.nn.Conv2d(32, 16, 5, stride=2, padding=0, bias=False), torch.nn.Tanh())

    def forward(self, x):
        return self.model(x)



func = ModelTanh().to('cpu')


x = torch.randn(2, 3, 8, 8)

test_inputs = [x]

# JIT_FAIL
'''
direct:
Calculated padded input size per channel: (12 x 12). Kernel size: (13 x 13). Kernel size can't be greater than actual input size

jit:
Failed running call_function <built-in method conv2d of type object at 0x7bca33996ec0>(*(FakeTensor(..., size=(2, 3, 8, 8)), Parameter(FakeTensor(..., size=(32, 3, 7, 7), requires_grad=True)), Parameter(FakeTensor(..., size=(32,), requires_grad=True)), (2, 2), (2, 2), (2, 2), 1), **{}):
Calculated padded input size per channel: (12 x 12). Kernel size: (13 x 13). Kernel size can't be greater than actual input size

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