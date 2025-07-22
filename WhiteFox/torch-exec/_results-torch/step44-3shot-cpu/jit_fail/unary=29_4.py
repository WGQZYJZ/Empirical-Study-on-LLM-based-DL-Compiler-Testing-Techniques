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

    def __init__(self, min_value=-18.131, max_value=-18.132):
        super().__init__()
        self.mul = torch.nn.quantized.FloatFunctional()
        self.conv_transpose = torch.nn.ConvTranspose2d(3, 4, 2, stride=2)
        self.min_value = torch.tensor(-18.131, dtype=torch.float32)
        self.max_value = torch.tensor(-18.132, dtype=torch.float32)

    def forward(self, x1, x2, x3, x4):
        v1 = self.conv_transpose(x1)
        v2 = self.conv_transpose(x2)
        v3 = self.min_value.to(x1.device)
        v4 = self.max_value.to(x1.device)
        v5 = (self.mul.mul(v3, x3), self.mul.mul(v4, x4))
        v6 = self.mul.add(v5[0], v5[1])
        v7 = torch.clamp_min(v1, v6)
        v8 = torch.clamp_max(v7, v6)
        return v8



func = Model().to('cpu')


x1 = torch.randn(1, 3, 32, 32)

x2 = torch.randn(1, 3, 32, 32)

x3 = torch.randn(1, 4)

x4 = torch.randn(1, 4)

test_inputs = [x1, x2, x3, x4]

# JIT_FAIL
'''
direct:
The size of tensor a (64) must match the size of tensor b (4) at non-singleton dimension 3

jit:
Failed running call_function <built-in method clamp_min of type object at 0x796da0d96ec0>(*(FakeTensor(..., size=(1, 4, 64, 64)), FakeTensor(..., size=(1, 4))), **{}):
Attempting to broadcast a dimension of length 4 at -1! Mismatching argument at index 1 had torch.Size([1, 4]); but expected shape should be broadcastable to [1, 4, 64, 64]

from user code:
   File "<string>", line 29, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''