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
        self.linear = torch.nn.Linear(5, 32)

    def forward(self, x1, x2, x3, x4, x5):
        v1 = self.linear(x1)
        v2 = v1 - x2
        v3 = F.relu(v2)
        v4 = v3 - x3
        v5 = F.relu(v4)
        v6 = v5 - x4
        v7 = F.relu(v6)
        v8 = v7 - x5
        v9 = F.relu(v8)
        return v9


func = Model().to('cpu')


x1 = torch.randn(1, 5)

x2 = torch.randn(1, 2)

x3 = torch.randn(1, 4)

x4 = torch.randn(1, 1)

x5 = torch.randn(1, 9)

test_inputs = [x1, x2, x3, x4, x5]

# JIT_FAIL
'''
direct:
The size of tensor a (32) must match the size of tensor b (2) at non-singleton dimension 1

jit:
Failed running call_function <built-in function sub>(*(FakeTensor(..., size=(1, 32)), FakeTensor(..., size=(1, 2))), **{}):
Attempting to broadcast a dimension of length 2 at -1! Mismatching argument at index 1 had torch.Size([1, 2]); but expected shape should be broadcastable to [1, 32]

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''