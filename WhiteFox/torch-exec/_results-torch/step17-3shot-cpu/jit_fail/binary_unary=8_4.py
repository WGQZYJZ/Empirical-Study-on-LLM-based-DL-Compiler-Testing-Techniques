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
        self.conv = torch.nn.Conv2d(3, 8, 3, stride=2, padding=0)
        self.conv1 = torch.nn.Conv2d(8, 8, 3, stride=2, padding=0)

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = self.conv1(v1)
        v3 = v1 + v2
        v4 = torch.relu(v3)
        return v4



func = Model().to('cpu')


x1 = torch.randn(1, 3, 64, 64)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
The size of tensor a (31) must match the size of tensor b (15) at non-singleton dimension 3

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., size=(1, 8, 31, 31)), FakeTensor(..., size=(1, 8, 15, 15))), **{}):
Attempting to broadcast a dimension of length 15 at -1! Mismatching argument at index 1 had torch.Size([1, 8, 15, 15]); but expected shape should be broadcastable to [1, 8, 31, 31]

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''