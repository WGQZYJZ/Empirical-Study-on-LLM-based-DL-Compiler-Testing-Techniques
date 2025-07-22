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
        self.conv4 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.conv5 = torch.nn.ConvTranspose2d(3, 8, 1, stride=1, padding=0)
        self.conv6 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.conv7 = torch.nn.Conv2d(3, 3, 1, stride=1, padding=1)

    def forward(self, x1, x2, x3, x4, x5):
        v1 = self.conv1(x1)
        v2 = self.conv2(x2)
        v3 = v1 + v2
        v4 = self.conv3(x3)
        v5 = self.conv4(x4)
        v6 = v3 + v5
        v7 = v6 + self.conv5(x5)
        v8 = self.conv6(v7)
        v9 = v8.squeeze(dim=1)
        v10 = self.conv7(v9)
        return v10



func = Model().to('cpu')


x1 = torch.randn(1, 3, 64, 64)

x2 = torch.randn(1, 3, 63, 63)

x3 = torch.randn(1, 3, 61, 61)

x4 = torch.randn(1, 3, 60, 60)

x5 = torch.randn(1, 3, 1, 1)

test_inputs = [x1, x2, x3, x4, x5]

# JIT_FAIL
'''
direct:
The size of tensor a (66) must match the size of tensor b (65) at non-singleton dimension 3

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., size=(1, 8, 66, 66)), FakeTensor(..., size=(1, 8, 65, 65))), **{}):
Attempting to broadcast a dimension of length 65 at -1! Mismatching argument at index 1 had torch.Size([1, 8, 65, 65]); but expected shape should be broadcastable to [1, 8, 66, 66]

from user code:
   File "<string>", line 28, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''