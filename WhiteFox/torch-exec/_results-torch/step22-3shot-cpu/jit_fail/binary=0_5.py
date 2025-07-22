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
        self.conv = torch.nn.Conv2d(32, 8, 1, stride=1, padding=1)

    def forward(self, x1, x2=None, padding1=None):
        if x2 == None:
            x2 = torch.randn(1, 32, 64, 64)
        v1 = self.conv(x1)
        if padding1 == None:
            padding1 = torch.randn(x2.shape)
        v2 = x2 + v1
        return v2



func = Model().to('cpu')


x1 = torch.randn(1, 32, 64, 64)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
The size of tensor a (64) must match the size of tensor b (66) at non-singleton dimension 3

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., size=(1, 32, 64, 64)), FakeTensor(..., size=(1, 8, 66, 66))), **{}):
Attempting to broadcast a dimension of length 66 at -1! Mismatching argument at index 1 had torch.Size([1, 8, 66, 66]); but expected shape should be broadcastable to [1, 32, 64, 64]

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''