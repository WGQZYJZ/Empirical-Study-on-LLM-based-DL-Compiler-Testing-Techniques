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
        self.linear = torch.nn.Linear(10, 10).to(torch.float32)
        self.conv = torch.nn.Conv2d(10, 10, 3).to(torch.float32)
        self.dropout = torch.nn.Dropout()

    def forward(self, inp, x1, x2):
        v1 = self.linear(inp)
        v2 = self.conv(x1)
        v3 = self.dropout(v2)
        v3 = v3 + x2
        return v3



func = Model().to('cpu')


inp = torch.randn(1, 10, requires_grad=True)

x1 = torch.randn(1, 10, 10, 10)

x2 = torch.randn(1, 10, 10, 10)

test_inputs = [inp, x1, x2]

# JIT_FAIL
'''
direct:
The size of tensor a (8) must match the size of tensor b (10) at non-singleton dimension 3

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., size=(1, 10, 8, 8)), FakeTensor(..., size=(1, 10, 10, 10))), **{}):
Attempting to broadcast a dimension of length 10 at -1! Mismatching argument at index 1 had torch.Size([1, 10, 10, 10]); but expected shape should be broadcastable to [1, 10, 8, 8]

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''