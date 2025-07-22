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
        self.conv_transpose = torch.nn.ConvTranspose2d(4, 6, 8, 1, 0, 0, 1, 2)

    def forward(self, x1):
        v1 = torch.sign(x1)
        v2 = self.conv_transpose(v1)
        v3 = v2 + 3
        v4 = torch.clamp(v3, min=0)
        v5 = torch.clamp(v4, max=6)
        v6 = torch.abs(v1)
        v7 = v6 * v5
        v8 = torch.abs(v7)
        v9 = v8 / 6
        return v9



func = Model().to('cpu')


x1 = torch.randn(1, 4, 2, 2)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
The size of tensor a (2) must match the size of tensor b (9) at non-singleton dimension 3

jit:
Failed running call_function <built-in function mul>(*(FakeTensor(..., size=(1, 4, s1, s2)), FakeTensor(..., size=(1, 6, s1 + 7, s2 + 7))), **{}):
The size of tensor a (s2) must match the size of tensor b (s2 + 7) at non-singleton dimension 3)

from user code:
   File "<string>", line 26, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''