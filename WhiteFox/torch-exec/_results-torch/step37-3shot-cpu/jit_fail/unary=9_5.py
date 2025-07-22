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
        self.conv1 = torch.nn.Conv2d(3, 3, 3, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(3, 3, 1, stride=1)
        self.conv3 = torch.nn.Conv2d(12, 1, 1)

    def forward(self, x1):
        x1_conv1 = self.conv1(x1)
        x1_conv2 = self.conv2(x1_conv1)
        x1_conv1_resize = torch.nn.functional.interpolate(x1_conv2, scale_factor=2)
        x = torch.cat([x1_conv1_resize, x1_conv1], dim=1)
        x1_conv3 = self.conv3(x)
        return x1_conv3



func = Model().to('cpu')


x1 = torch.randn(1, 3, 64, 64)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Sizes of tensors must match except in dimension 1. Expected size 128 but got size 64 for tensor number 1 in the list.

jit:
Failed running call_function <built-in method cat of type object at 0x738f50d96ec0>(*([FakeTensor(..., size=(1, 3, 128, 128)), FakeTensor(..., size=(1, 3, 64, 64))],), **{'dim': 1}):
Sizes of tensors must match except in dimension 1. Expected 128 in dimension 2 but got 64 for tensor number 1 in the list

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''