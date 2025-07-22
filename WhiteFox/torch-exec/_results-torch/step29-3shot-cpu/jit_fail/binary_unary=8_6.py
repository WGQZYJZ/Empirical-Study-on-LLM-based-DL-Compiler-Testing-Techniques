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
        self.conv = torch.nn.Conv2d(3, 8, 3, stride=1, padding=0)

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.tanh(v1 + x1)
        v3 = torch.relu(v1 + x1)
        v4 = torch.relu(v1 + x1)
        v5 = torch.sigmoid(v1 + x1)
        v6 = v2 + v3 + v4 + v5
        v7 = torch.relu(v1 + x1)
        v8 = torch.tanh(v1 + x1)
        v9 = torch.relu(v1 + x1)
        v10 = v7 + v8 + v9
        res = torch.relu(v10)
        return res



func = Model().to('cpu')


x1 = torch.randn(1, 3, 64, 64)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
The size of tensor a (62) must match the size of tensor b (64) at non-singleton dimension 3

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., size=(1, 8, 62, 62)), FakeTensor(..., size=(1, 3, 64, 64))), **{}):
Attempting to broadcast a dimension of length 64 at -1! Mismatching argument at index 1 had torch.Size([1, 3, 64, 64]); but expected shape should be broadcastable to [1, 8, 62, 62]

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''