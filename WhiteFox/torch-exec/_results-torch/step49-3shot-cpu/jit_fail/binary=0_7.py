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
        self.conv = torch.nn.Conv2d(48, 4, 1, stride=1, padding=1)

    def forward(self, x1, other, other1=None):
        v1 = self.conv(x1)
        if other1 is not None:
            v2 = other1
        else:
            v2 = torch.randn(1, 8, 64, 64)
        v2 += v1
        other = other // v1
        return v2



func = Model().to('cpu')


x1 = torch.randn(1, 48, 64, 64)
other = 1

test_inputs = [x1, other]

# JIT_FAIL
'''
direct:
The size of tensor a (64) must match the size of tensor b (66) at non-singleton dimension 3

jit:
Failed running call_function <built-in function iadd>(*(FakeTensor(..., size=(1, 8, 64, 64)), FakeTensor(..., size=(1, 4, s1 + 2, s2 + 2))), **{}):
Attempting to broadcast a dimension of length s2 + 2 at -1! Mismatching argument at index 1 had torch.Size([1, 4, s1 + 2, s2 + 2]); but expected shape should be broadcastable to [1, 8, 64, 64]

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''