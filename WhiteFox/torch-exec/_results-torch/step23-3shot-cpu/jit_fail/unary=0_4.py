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
        self.conv1 = torch.nn.Conv2d(32, 64, 1, padding=0, dilation=1, groups=1, bias=False)
        self.conv2 = torch.nn.Conv2d(64, 128, 1, padding=0, dilation=1, groups=1, bias=False)

    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = self.conv2(v1)
        v3 = v2 + v1
        return v3



func = Model().to('cpu')


x1 = torch.randn(1, 32, 32, 32)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
The size of tensor a (128) must match the size of tensor b (64) at non-singleton dimension 1

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., size=(1, 128, 32, 32)), FakeTensor(..., size=(1, 64, 32, 32))), **{}):
Attempting to broadcast a dimension of length 64 at -3! Mismatching argument at index 1 had torch.Size([1, 64, 32, 32]); but expected shape should be broadcastable to [1, 128, 32, 32]

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''