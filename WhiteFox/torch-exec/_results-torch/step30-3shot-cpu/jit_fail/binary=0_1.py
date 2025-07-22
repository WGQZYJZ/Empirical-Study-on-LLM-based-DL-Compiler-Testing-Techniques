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
        self.conv = torch.nn.Conv2d(3, 8, 3, stride=1, padding=1)

    def forward(self, x1, padding1=1):
        v1 = self.conv(x1)
        if padding1 == 1:
            padding1 = torch.randn(v1.shape[:-1])
        else:
            padding1 = torch.randn(v1.shape[:-1])
        v2 = v1 + padding1
        return v2



func = Model().to('cpu')


x1 = torch.randn(1, 3, 64, 64)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
The size of tensor a (64) must match the size of tensor b (8) at non-singleton dimension 2

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., size=(1, 8, 64, 64)), FakeTensor(..., size=(1, 8, 64))), **{}):
Attempting to broadcast a dimension of length 8 at -2! Mismatching argument at index 1 had torch.Size([1, 8, 64]); but expected shape should be broadcastable to [1, 8, 64, 64]

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''