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
        self.linear = torch.nn.Linear(3, 6)

    def forward(self, x1, x2, x3):
        v2 = x2 + x2
        v3 = x3 + x3
        v4 = v2 + v3
        v5 = self.linear(x1)
        v6 = v4 + v5
        return v6


func = Model().to('cpu')


x1 = torch.randn(1, 3)

x2 = torch.randn(1, 3)

x3 = torch.randn(1, 3)

test_inputs = [x1, x2, x3]

# JIT_FAIL
'''
direct:
The size of tensor a (3) must match the size of tensor b (6) at non-singleton dimension 1

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., size=(1, 3)), FakeTensor(..., size=(1, 6))), **{}):
Attempting to broadcast a dimension of length 6 at -1! Mismatching argument at index 1 had torch.Size([1, 6]); but expected shape should be broadcastable to [1, 3]

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''