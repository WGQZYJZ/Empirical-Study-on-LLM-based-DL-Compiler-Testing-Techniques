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
        self.conv_t = torch.nn.ConvTranspose2d(1, 3, 1, stride=1, padding=1)
        self.pooling = torch.nn.AvgPool2d(2, stride=2)

    def forward(self, x4):
        x1 = self.conv_t(x4)
        x7 = self.pooling(x1)
        x6 = x1 > 0
        x3 = x1 * 0.7
        x5 = torch.where(x6, x1, x3)
        x8 = torch.tanh(x5)
        x9 = torch.cat((x7, x5), 1)
        return x9



func = Model().to('cpu')


x4 = torch.randn(8, 1, 16, 16)

test_inputs = [x4]

# JIT_FAIL
'''
direct:
Sizes of tensors must match except in dimension 1. Expected size 7 but got size 14 for tensor number 1 in the list.

jit:
Failed running call_function <built-in method cat of type object at 0x7fad33196ec0>(*((FakeTensor(..., size=(8, 3, 7, 7)), FakeTensor(..., size=(8, 3, 14, 14))), 1), **{}):
Sizes of tensors must match except in dimension 1. Expected 7 in dimension 2 but got 14 for tensor number 1 in the list

from user code:
   File "<string>", line 27, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''