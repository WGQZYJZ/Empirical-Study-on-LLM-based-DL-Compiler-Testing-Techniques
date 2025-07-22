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
        self.conv1 = torch.nn.Conv2d(in_channels=1, out_channels=1, kernel_size=(1, 15), stride=(1, 1), padding=(0, 7))
        self.conv2 = torch.nn.Conv2d(in_channels=1, out_channels=1, kernel_size=(1, 15), stride=(1, 1), padding=(0, 13))

    def forward(self, x1):
        x2 = self.conv1(x1)
        x3 = torch.sigmoid(x2)
        x4 = self.conv2(x3)
        x5 = torch.sigmoid(x4)
        x6 = torch.cat([x1, x5], dim=1)
        return x6



func = Model().to('cpu')


x1 = torch.randn(1, 1, 256, 288)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Sizes of tensors must match except in dimension 1. Expected size 288 but got size 300 for tensor number 1 in the list.

jit:
Failed running call_function <built-in method cat of type object at 0x795533d96ec0>(*([FakeTensor(..., size=(1, 1, s0, s1)), FakeTensor(..., size=(1, 1, s0, s1 + 12))],), **{'dim': 1}):
Sizes of tensors must match except in dimension 1. Expected s1 in dimension 3 but got s1 + 12 for tensor number 1 in the list

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''