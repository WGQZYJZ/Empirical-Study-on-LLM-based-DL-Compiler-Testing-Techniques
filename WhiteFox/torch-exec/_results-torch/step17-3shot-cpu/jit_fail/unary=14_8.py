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
        self.conv_transpose1 = torch.nn.ConvTranspose2d(8, 8, 3, stride=2, padding=0)
        self.conv_transpose2 = torch.nn.ConvTranspose2d(8, 8, 1, stride=2, padding=0)
        self.conv_transpose3 = torch.nn.ConvTranspose2d(8, 8, 5, stride=2, padding=0)

    def forward(self, x1):
        v1 = self.conv_transpose1(x1)
        v2 = torch.sigmoid(v1)
        v3 = v1 * v2
        v4 = self.conv_transpose2(x1)
        v5 = torch.sigmoid(v4)
        v6 = v4 * v5
        v7 = self.conv_transpose3(x1)
        v8 = torch.sigmoid(v7)
        v9 = v7 * v8
        v15 = v3 + v6 + v9
        return v15



func = Model().to('cpu')


x1 = torch.randn(1, 8, 32, 32)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
The size of tensor a (65) must match the size of tensor b (63) at non-singleton dimension 3

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., size=(1, 8, 65, 65)), FakeTensor(..., size=(1, 8, 63, 63))), **{}):
Attempting to broadcast a dimension of length 63 at -1! Mismatching argument at index 1 had torch.Size([1, 8, 63, 63]); but expected shape should be broadcastable to [1, 8, 65, 65]

from user code:
   File "<string>", line 31, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''