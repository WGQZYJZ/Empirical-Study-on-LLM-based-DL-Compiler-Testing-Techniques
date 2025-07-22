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
        self.conv = torch.nn.Conv2d(8, 64, 2, stride=1, padding=1)
        self.bn = torch.nn.BatchNorm2d(64)

    def forward(self, x, y):
        v1 = self.conv(x)
        v2 = v1 * 0.5
        v3 = y * v1
        v4 = v3 * v1
        v5 = v4 * 0.044715
        v6 = v1 + v5
        v7 = v6 * 0.7978845608028654
        v8 = torch.tanh(v7)
        v9 = v8 + 1
        v10 = v2 * v9
        return v10



func = Model().to('cpu')


x = torch.randn(1, 8, 255, 255)

y = torch.randn(1, 8, 111, 111)

test_inputs = [x, y]

# JIT_FAIL
'''
direct:
The size of tensor a (111) must match the size of tensor b (256) at non-singleton dimension 3

jit:
Failed running call_function <built-in function mul>(*(FakeTensor(..., size=(1, 8, 111, 111)), FakeTensor(..., size=(1, 64, 256, 256))), **{}):
Attempting to broadcast a dimension of length 256 at -1! Mismatching argument at index 1 had torch.Size([1, 64, 256, 256]); but expected shape should be broadcastable to [1, 8, 111, 111]

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''