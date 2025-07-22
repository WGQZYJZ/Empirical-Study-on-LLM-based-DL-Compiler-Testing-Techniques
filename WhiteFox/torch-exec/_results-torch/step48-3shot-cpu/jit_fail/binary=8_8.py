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
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.conv3 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.bn1 = torch.nn.BatchNorm2d(8)
        self.bn2 = torch.nn.BatchNorm2d(8)
        self.bn3 = torch.nn.BatchNorm2d(8)
        self.conv4 = torch.nn.Conv2d(8, 8, 1, stride=1, padding=1)

    def forward(self, x1, x2, x3):
        v1 = self.conv1(x1)
        v2 = self.conv2(x2)
        v3 = self.conv3(x3)
        v4 = v1 + v2
        v11 = v2 + v3
        v5 = self.bn1(v4)
        v6 = self.bn2(v4)
        v12 = self.bn3(v11)
        v7 = torch.sigmoid(v5)
        v8 = torch.sigmoid(v12)
        v9 = torch.tanh(v8)
        v10 = self.conv4(v9)
        return v7 * v10



func = Model().to('cpu')


x1 = torch.randn(1, 3, 64, 64)

x2 = torch.randn(1, 3, 64, 64)

x3 = torch.randn(1, 3, 64, 64)

test_inputs = [x1, x2, x3]

# JIT_FAIL
'''
direct:
The size of tensor a (66) must match the size of tensor b (68) at non-singleton dimension 3

jit:
Failed running call_function <built-in function mul>(*(FakeTensor(..., size=(1, 8, 66, 66)), FakeTensor(..., size=(1, 8, 68, 68))), **{}):
Attempting to broadcast a dimension of length 68 at -1! Mismatching argument at index 1 had torch.Size([1, 8, 68, 68]); but expected shape should be broadcastable to [1, 8, 66, 66]

from user code:
   File "<string>", line 38, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''