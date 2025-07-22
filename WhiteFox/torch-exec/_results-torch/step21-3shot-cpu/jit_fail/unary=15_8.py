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
        self.conv = torch.nn.Conv2d(3, 8, 3, stride=1, padding=1)
        self.weight_0 = torch.nn.Parameter(torch.FloatTensor([[[[0.1, 0.2, 0.1], [0.2, 0.001, 0.2], [0.1, 0.2, 0.5]]]]))

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.nn.functional.conv2d(input=x1, weight=self.weight_0, bias=None, stride=1, padding=1, dilation=1, groups=1)
        v3 = torch.nn.functional.interpolate(size=[64, 64])(torch.nn.functional.interpolate(v1, size=[64, 64], align_corners=True) + v2)
        return v3



func = Model().to('cpu')


x1 = torch.randn(1, 3, 32, 32)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [1, 1, 3, 3], expected input[1, 3, 32, 32] to have 1 channels, but got 3 channels instead

jit:
Failed running call_function <built-in method conv2d of type object at 0x7dfd2af96ec0>(*(), **{'input': FakeTensor(..., size=(1, 3, 32, 32)), 'weight': Parameter(FakeTensor(..., size=(1, 1, 3, 3), requires_grad=True)), 'bias': None, 'stride': 1, 'padding': 1, 'dilation': 1, 'groups': 1}):
Given groups=1, weight of size [1, 1, 3, 3], expected input[1, 3, 32, 32] to have 1 channels, but got 3 channels instead

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''