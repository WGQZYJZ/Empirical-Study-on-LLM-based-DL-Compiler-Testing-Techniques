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
        self.conv_t = torch.nn.ConvTranspose2d(476, 338, 2, stride=1, padding=0, bias=False)

    def forward(self, x5):
        v1 = self.conv_t(x5)
        v2 = v1 > 0
        v3 = v1 * 0.4987
        v4 = torch.where(v2, v1, v3)
        v5 = v4 + torch.nn.functional.upsample_bilinear(v4, (13, 31))
        return v4



func = Model().to('cpu')


x5 = torch.randn(13, 476, 6, 32)

test_inputs = [x5]

# JIT_FAIL
'''
direct:
The size of tensor a (33) must match the size of tensor b (31) at non-singleton dimension 3

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., size=(s0, 338, s2 + 1, s3 + 1)), FakeTensor(..., size=(s0, 338, 13, 31))), **{}):
The size of tensor a (s3 + 1) must match the size of tensor b (31) at non-singleton dimension 3)

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''