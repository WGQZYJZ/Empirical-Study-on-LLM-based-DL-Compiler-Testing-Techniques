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
        self.linear = torch.nn.Linear(128, 64)

    def forward(self, x, x2):
        v1 = self.linear(x)
        v2 = torch.tanh(v1)
        v3 = v2 * x2
        return v3


func = Model().to('cpu')


x = torch.randn(128, 128)

x2 = torch.randn(128, 128)

test_inputs = [x, x2]

# JIT_FAIL
'''
direct:
The size of tensor a (64) must match the size of tensor b (128) at non-singleton dimension 1

jit:
Failed running call_function <built-in function mul>(*(FakeTensor(..., size=(128, 64)), FakeTensor(..., size=(128, 128))), **{}):
Attempting to broadcast a dimension of length 128 at -1! Mismatching argument at index 1 had torch.Size([128, 128]); but expected shape should be broadcastable to [128, 64]

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''