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
        self.conv_weight = torch.nn.Parameter(torch.randn(8, 3))
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x1):
        v1 = torch.conv2d(x1, self.conv_weight, bias=None, stride=1, padding=1, dilation=1, groups=1)
        v2 = v1 - torch.exp(torch.arange(8.0, 16.0))
        return v2



func = Model().to('cpu')


x1 = torch.randn(1, 3, 64, 64)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
weight should have at least three dimensions

jit:
Failed running call_function <built-in method conv2d of type object at 0x75d537b96ec0>(*(FakeTensor(..., size=(1, 3, 64, 64)), Parameter(FakeTensor(..., size=(8, 3), requires_grad=True))), **{'bias': None, 'stride': 1, 'padding': 1, 'dilation': 1, 'groups': 1}):
expected stride to be a single integer value or a list of 0 values to match the convolution dimensions, but got stride=[1, 1]

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''