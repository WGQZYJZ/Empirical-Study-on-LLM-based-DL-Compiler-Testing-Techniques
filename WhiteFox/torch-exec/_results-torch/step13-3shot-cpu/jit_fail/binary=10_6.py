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
        self.linear = torch.nn.Linear(5, 2)
        self._other = torch.from_numpy(other)

    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 + self._other
        return v2


other = 1
func = Model(np.random.rand(1, 5)).to('cpu')


x1 = torch.randn(1, 1, 5)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
The size of tensor a (2) must match the size of tensor b (5) at non-singleton dimension 2

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., size=(1, 1, 2)), FakeTensor(..., size=(1, 5), dtype=torch.float64)), **{}):
Attempting to broadcast a dimension of length 5 at -1! Mismatching argument at index 1 had torch.Size([1, 5]); but expected shape should be broadcastable to [1, 1, 2]

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''