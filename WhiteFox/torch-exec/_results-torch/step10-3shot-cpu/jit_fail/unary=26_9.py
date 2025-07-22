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
        self.conv_transpose_2 = torch.nn.ConvTranspose2d(3, 8, 1, stride=1, padding=0)
        self.conv_transpose_1 = torch.nn.ConvTranspose2d(3, 8, 1, stride=1, padding=1)
        self.addm = torch.nn.ReLU()

    def forward(self, x1):
        x2 = self.conv_transpose_2(x1)
        x3 = self.conv_transpose_1(x1)
        x4 = x2 + x3
        x5 = x4 > 0
        x6 = self.addm(x4)
        x7 = torch.where(x5, x4, x6)
        return x7



func = Model().to('cpu')


x1 = torch.randn(1, 3, 64, 64)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
The size of tensor a (64) must match the size of tensor b (62) at non-singleton dimension 3

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., size=(1, 8, 64, 64)), FakeTensor(..., size=(1, 8, 62, 62))), **{}):
Attempting to broadcast a dimension of length 62 at -1! Mismatching argument at index 1 had torch.Size([1, 8, 62, 62]); but expected shape should be broadcastable to [1, 8, 64, 64]

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''