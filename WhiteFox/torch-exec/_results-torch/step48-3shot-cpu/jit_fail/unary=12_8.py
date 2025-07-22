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
        self.conv = torch.nn.Conv2d(6, 2, 1, stride=1, padding=0)
        self.pad = torch.nn.ZeroPad2d(2)
        self.sigmoid = torch.nn.Sigmoid()
        self.multiply = torch.mul

    def forward(self, x1):
        v1 = self.pad(x1)
        v2 = self.conv(v1)
        v3 = self.sigmoid(v2)
        v4 = v1 * v2
        return v3 * v4



func = Model().to('cpu')


x1 = torch.randn(1, 6, 64, 64)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
The size of tensor a (6) must match the size of tensor b (2) at non-singleton dimension 1

jit:
Failed running call_function <built-in function mul>(*(FakeTensor(..., size=(1, 6, 68, 68)), FakeTensor(..., size=(1, 2, 68, 68))), **{}):
Attempting to broadcast a dimension of length 2 at -3! Mismatching argument at index 1 had torch.Size([1, 2, 68, 68]); but expected shape should be broadcastable to [1, 6, 68, 68]

from user code:
   File "<string>", line 26, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''