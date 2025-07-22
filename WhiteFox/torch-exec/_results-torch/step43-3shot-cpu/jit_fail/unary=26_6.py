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
        self.input = torch.nn.Parameter(torch.randn(32768, requires_grad=True))
        self.conv_t = torch.nn.ConvTranspose1d(6, 11, 1, stride=1, padding=0, bias=False)
        self.conv_t.requires_grad = False

    def forward(self, x14):
        v0 = self.input
        l1 = torch.tanh(self.conv_t(x14))
        l2 = l1 > 0
        l3 = l1 * -0.475
        l4 = torch.where(l2, l1, l3)
        j4 = torch.clamp(v0 * l4, min=-1.0, max=1.0)
        return j4



func = Model().to('cpu')


x14 = torch.randn(123, 6)

test_inputs = [x14]

# JIT_FAIL
'''
direct:
Given transposed=1, weight of size [6, 11, 1], expected input[1, 123, 6] to have 6 channels, but got 123 channels instead

jit:
Failed running call_function <built-in function mul>(*(Parameter(FakeTensor(..., size=(32768,), requires_grad=True)), FakeTensor(..., size=(11, 6))), **{}):
Attempting to broadcast a dimension of length 6 at -1! Mismatching argument at index 1 had torch.Size([11, 6]); but expected shape should be broadcastable to [1, 32768]

from user code:
   File "<string>", line 27, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''