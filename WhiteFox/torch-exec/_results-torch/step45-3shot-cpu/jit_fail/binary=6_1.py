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
        self.linear = torch.nn.Linear(16, 64)

    def forward(self, x1, x2):
        v1 = self.linear(x2)
        v2 = v1 - x1
        return v2


func = Model().to('cpu')


x1 = torch.randn(1, 512, 7, 7)

x2 = torch.randn(2, 16)

test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
The size of tensor a (64) must match the size of tensor b (7) at non-singleton dimension 3

jit:
Failed running call_function <built-in function sub>(*(FakeTensor(..., size=(2, 64)), FakeTensor(..., size=(1, 512, 7, 7))), **{}):
Attempting to broadcast a dimension of length 7 at -1! Mismatching argument at index 1 had torch.Size([1, 512, 7, 7]); but expected shape should be broadcastable to [1, 1, 2, 64]

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''