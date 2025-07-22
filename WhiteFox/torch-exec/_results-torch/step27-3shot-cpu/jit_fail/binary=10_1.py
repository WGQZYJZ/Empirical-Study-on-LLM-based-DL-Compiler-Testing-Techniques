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

    def __init__(self, out_features):
        super().__init__()
        self.linear = torch.nn.Linear(32, out_features)

    def forward(self, x1, other=None):
        v1 = self.linear(x1)
        if other is None:
            v1 = v1 + torch.abs(x1)
        else:
            v1 = v1 + other
        return v1


out_features = 1
func = Model(8).to('cpu')


x1 = torch.randn(1, 32)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
The size of tensor a (8) must match the size of tensor b (32) at non-singleton dimension 1

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., size=(1, 8)), FakeTensor(..., size=(1, 32))), **{}):
Attempting to broadcast a dimension of length 32 at -1! Mismatching argument at index 1 had torch.Size([1, 32]); but expected shape should be broadcastable to [1, 8]

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''