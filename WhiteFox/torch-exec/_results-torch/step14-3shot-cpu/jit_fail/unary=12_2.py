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
        self.conv = torch.nn.Conv2d(3, 16, 1, stride=1, padding=0, dilation=1)
        self.pointwise_conv = torch.nn.Conv2d(16, 3, 1)

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1.sigmoid()
        v3 = v1 * v2
        v4 = self.pointwise_conv(v1)
        v5 = v4.clamp(min=0, max=256)
        v6 = v3 * v5
        return v6



func = Model().to('cpu')


x1 = torch.randn(1, 3, 64, 64)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
The size of tensor a (16) must match the size of tensor b (3) at non-singleton dimension 1

jit:
Failed running call_function <built-in function mul>(*(FakeTensor(..., size=(1, 16, 64, 64)), FakeTensor(..., size=(1, 3, 64, 64))), **{}):
Attempting to broadcast a dimension of length 3 at -3! Mismatching argument at index 1 had torch.Size([1, 3, 64, 64]); but expected shape should be broadcastable to [1, 16, 64, 64]

from user code:
   File "<string>", line 26, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''