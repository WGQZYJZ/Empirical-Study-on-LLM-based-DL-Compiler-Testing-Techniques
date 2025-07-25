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
        self.conv = torch.nn.Conv2d(8, 64, 2, stride=2, padding=1)
        self.conv1 = torch.nn.Conv2d(64, 64, 2, stride=2, padding=1)
        self.conv2 = torch.nn.Conv2d(64, 128, 1, stride=1, padding=0)
        self.conv3 = torch.nn.Conv2d(128, 128, 1, stride=1, padding=0)
        self.conv4 = torch.nn.Conv2d(128, 128, 1, stride=1, padding=0)
        self.conv5 = torch.nn.Conv2d(128, 256, 1, stride=1, padding=0)
        self.conv6 = torch.nn.Conv2d(256, 256, 1, stride=1, padding=0)
        self.conv7 = torch.nn.Conv2d(256, 256, 1, stride=1, padding=0)
        self.conv8 = torch.nn.Conv2d(256, 512, 1, stride=1, padding=0)

    def forward(self, x2):
        v1 = self.conv(x2)
        v2 = self.conv1(v1)
        v3 = self.conv2(v2)
        v4 = self.conv3(v3)
        v5 = self.conv4(v4)
        v6 = torch.cat([v1, v2, v3, v4, v5], dim=1)
        v7 = self.conv5(v6)
        v8 = self.conv6(v7)
        v9 = self.conv7(v8)
        v10 = self.conv8(v9)
        v11 = v10 * 0.5
        v12 = v10 * v10
        v13 = v12 * v10
        v14 = v13 * 0.044715
        v15 = v10 + v14
        v16 = v15 * 0.7978845608028654
        v17 = torch.tanh(v16)
        v18 = v17 + 1
        v19 = v11 * v18
        return v19



func = Model().to('cpu')


x2 = torch.randn(1, 8, 32, 32)

test_inputs = [x2]

# JIT_FAIL
'''
direct:
Sizes of tensors must match except in dimension 1. Expected size 17 but got size 9 for tensor number 1 in the list.

jit:
Failed running call_function <built-in method cat of type object at 0x7d09b3396ec0>(*([FakeTensor(..., size=(1, 64, 17, 17)), FakeTensor(..., size=(1, 64, 9, 9)), FakeTensor(..., size=(1, 128, 9, 9)), FakeTensor(..., size=(1, 128, 9, 9)), FakeTensor(..., size=(1, 128, 9, 9))],), **{'dim': 1}):
Sizes of tensors must match except in dimension 1. Expected 17 in dimension 2 but got 9 for tensor number 1 in the list

from user code:
   File "<string>", line 33, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''