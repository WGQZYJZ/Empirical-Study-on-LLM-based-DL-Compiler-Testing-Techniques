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

    def __init__(self, other):
        super().__init__()
        self.linear = torch.nn.Linear(16, 32)
        self.other = torch.nn.Parameter(other)

    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 + self.other
        return v2


other = 1
func = Model(torch.randn(128, 16)).to('cpu')


x1 = torch.randn(32, 16)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
The size of tensor a (32) must match the size of tensor b (16) at non-singleton dimension 1

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., size=(32, 32)), Parameter(FakeTensor(..., size=(128, 16), requires_grad=True))), **{}):
Attempting to broadcast a dimension of length 16 at -1! Mismatching argument at index 1 had torch.Size([128, 16]); but expected shape should be broadcastable to [32, 32]

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''