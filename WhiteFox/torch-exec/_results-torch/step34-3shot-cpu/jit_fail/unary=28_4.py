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

    def __init__(self, min_value=0.0, max_value=1.0):
        super().__init__()

    def forward(self, x1):
        v1 = x1 * x2
        v2 = torch.clamp_min(v1, self.min_value)
        v3 = torch.clamp_max(v2, self.max_value)
        return v3


func = Model().to('cpu')


x1 = torch.randn(1, 3, 64, 64)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
The size of tensor a (64) must match the size of tensor b (500) at non-singleton dimension 3

jit:
Failed running call_function <built-in function mul>(*(FakeTensor(..., size=(1, 3, 64, 64)), FakeTensor(..., size=(5, 3, 500, 500))), **{}):
Attempting to broadcast a dimension of length 500 at -1! Mismatching argument at index 1 had torch.Size([5, 3, 500, 500]); but expected shape should be broadcastable to [1, 3, 64, 64]

from user code:
   File "<string>", line 19, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''