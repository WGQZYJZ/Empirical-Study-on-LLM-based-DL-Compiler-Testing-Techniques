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
        self.conv = torch.nn.Conv2d(7, 24, 4, stride=1, padding=0)
        self.conv_transpose = torch.nn.ConvTranspose2d(24, 16, 3, stride=1, padding=0)

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = self.conv_transpose(v1)
        v3 = v2 + 3
        v4 = torch.clamp(v3, min=0)
        v5 = torch.clamp(v4, max=6)
        v6 = v1 * v5
        v7 = v6 / 6
        return v7



func = Model().to('cpu')


x1 = torch.randn(1, 7, 11, 13)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
The size of tensor a (10) must match the size of tensor b (12) at non-singleton dimension 3

jit:
Failed running call_function <built-in function mul>(*(FakeTensor(..., size=(1, 24, 8, 10)), FakeTensor(..., size=(1, 16, 10, 12))), **{}):
Attempting to broadcast a dimension of length 12 at -1! Mismatching argument at index 1 had torch.Size([1, 16, 10, 12]); but expected shape should be broadcastable to [1, 24, 8, 10]

from user code:
   File "<string>", line 26, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''