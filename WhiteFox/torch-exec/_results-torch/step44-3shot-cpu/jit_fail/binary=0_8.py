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
        self.conv1 = torch.nn.Conv2d(5, 5, 3, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(5, 5, 3, stride=1, padding=1)

    def forward(self, x1, other=3, padding1=3):
        v1 = self.conv1(x1)
        v2 = self.conv2(x1)
        if padding1 == 3:
            padding1 = torch.randn(v1.shape)
        v3 = v1 + other
        v4 = torch.cat([v3, padding1]) + v2
        return v4



func = Model().to('cpu')


x1 = torch.randn(2, 5, 64, 64)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
The size of tensor a (4) must match the size of tensor b (2) at non-singleton dimension 0

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., size=(2*s0, 5, s2, s3)), FakeTensor(..., size=(s0, 5, s2, s3))), **{}):
The size of tensor a (2*s0) must match the size of tensor b (s0) at non-singleton dimension 0)

from user code:
   File "<string>", line 26, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''