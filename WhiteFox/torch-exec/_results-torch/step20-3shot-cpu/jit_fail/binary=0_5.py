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
        self.conv = torch.nn.Conv2d(4, 8, 1, stride=1, padding=1)

    def forward(self, x1, other, padding1):
        v1 = self.conv(x1)
        if padding1 == None:
            padding1 = torch.randn(v1.shape)
        v2 = v1 + other
        return v2



func = Model().to('cpu')


x1 = torch.randn(1, 4, 64, 64)

other = torch.randn(1, 8, 64, 64)
padding1 = 1

test_inputs = [x1, other, padding1]

# JIT_FAIL
'''
direct:
The size of tensor a (66) must match the size of tensor b (64) at non-singleton dimension 3

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., size=(1, 8, s1 + 2, s2 + 2)), FakeTensor(..., size=(1, s3, s4, s5))), **{}):
The size of tensor a (s2 + 2) must match the size of tensor b (s5) at non-singleton dimension 3)

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''