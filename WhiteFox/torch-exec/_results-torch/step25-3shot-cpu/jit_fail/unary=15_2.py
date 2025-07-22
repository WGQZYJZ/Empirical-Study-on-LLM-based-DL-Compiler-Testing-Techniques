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

class Encoder1(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(1, 32, 3, stride=2, padding=1)
        self.conv2 = torch.nn.Conv2d(32, 32, 3, stride=1, padding=1)
        self.conv3 = torch.nn.Conv2d(32, 32, 3, stride=2, padding=1)
        self.conv4 = torch.nn.Conv2d(32, 32, 3, stride=1, padding=1)
        self.conv5 = torch.nn.Conv2d(32, 32, 3, stride=1, padding=1)

    def forward(self, x1):
        v1 = self.conv1(x1)
        v1_out = torch.relu(v1)
        v2 = self.conv4(v1_out)
        v3 = self.conv3(v2)
        v4 = self.conv5(v2)
        v5 = torch.cat((v3, v4), 1)
        return v5

class Decoder1(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(32, 32, 3, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(32, 32, 3, stride=1, padding=1)
        self.conv3 = torch.nn.Conv2d(32, 32, 3, stride=2, padding=1)
        self.conv4 = torch.nn.Conv2d(32, 32, 3, stride=1, padding=1)
        self.conv5 = torch.nn.Conv2d(32, 32, 3, stride=1, padding=1)
        self.conv6 = torch.nn.Conv2d(64, 3, 3, stride=1, padding=1)

    def forward(self, x1):
        v6 = x1
        v7 = self.conv3(v6)
        v8 = self.conv4(v7)
        v9 = self.conv5(v6)
        v10 = torch.cat((v8, v9), 1)
        v10_out = torch.relu(v10)
        v11 = self.conv1(v10_out)
        v12 = self.conv2(v11)
        v13 = self.conv6(v12)
        return v13

class Model(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.encoder1 = Encoder1()
        self.decoder1 = Decoder1()

    def forward(self, x1):
        v14 = self.encoder1(x1)
        v15 = self.decoder1(v14)
        return v15



func = Model().to('cpu')


x1 = torch.randn(2, 1, 256, 256)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Sizes of tensors must match except in dimension 1. Expected size 64 but got size 128 for tensor number 1 in the list.

jit:
Failed running call_function <built-in method cat of type object at 0x70fb5b596ec0>(*((FakeTensor(..., size=(2, 32, 64, 64)), FakeTensor(..., size=(2, 32, 128, 128))), 1), **{}):
Sizes of tensors must match except in dimension 1. Expected 64 in dimension 2 but got 128 for tensor number 1 in the list

from user code:
   File "<string>", line 63, in forward
  File "<string>", line 29, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''