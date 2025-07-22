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
        self.conv_transpose_1 = torch.nn.ConvTranspose2d(7, 8, 2, stride=2, padding=1)
        self.sigmoid_1 = torch.nn.Sigmoid()
        self.conv_transpose_2 = torch.nn.ConvTranspose2d(8, 6, 1, stride=1, padding=1)

    def forward(self, x1):
        v1 = self.conv_transpose_1(x1)
        v2 = self.sigmoid_1(v1)
        v3 = self.conv_transpose_2(v1)
        v4 = self.sigmoid_1(v3)
        v5 = v4 + v2
        return v5



func = Model().to('cpu')


x1 = torch.randn(1, 7, 64, 64)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
The size of tensor a (124) must match the size of tensor b (126) at non-singleton dimension 3

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., size=(1, 6, 124, 124)), FakeTensor(..., size=(1, 8, 126, 126))), **{}):
Attempting to broadcast a dimension of length 126 at -1! Mismatching argument at index 1 had torch.Size([1, 8, 126, 126]); but expected shape should be broadcastable to [1, 6, 124, 124]

from user code:
   File "<string>", line 26, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''