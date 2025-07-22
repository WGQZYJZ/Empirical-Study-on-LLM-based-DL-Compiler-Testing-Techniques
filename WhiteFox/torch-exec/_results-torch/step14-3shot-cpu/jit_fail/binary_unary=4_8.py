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
        self.linear1 = torch.nn.Linear(128, 64, bias=True)
        self.linear2 = torch.nn.Linear(64, 32, bias=True)
        self.linear3 = torch.nn.Linear(32, 8, bias=True)

    def forward(self, x, other):
        v1 = self.linear1(x)
        v2 = v1 + other
        v3 = F.relu(v2)
        v4 = self.linear2(v3)
        v5 = v4 + other
        v6 = F.relu(v5)
        v7 = self.linear3(v6)
        v8 = v7 + other
        return v8


func = Model().to('cpu')


x = torch.empty(1, 128)

other = torch.empty(1, 8)

test_inputs = [x, other]

# JIT_FAIL
'''
direct:
The size of tensor a (64) must match the size of tensor b (8) at non-singleton dimension 1

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., size=(1, 64)), FakeTensor(..., size=(1, 8))), **{}):
Attempting to broadcast a dimension of length 8 at -1! Mismatching argument at index 1 had torch.Size([1, 8]); but expected shape should be broadcastable to [1, 64]

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''