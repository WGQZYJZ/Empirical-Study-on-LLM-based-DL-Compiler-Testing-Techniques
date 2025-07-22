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
        self.linear = torch.nn.Linear(256, 512, bias=False)
        self.other = torch.nn.Parameter(torch.randn(256, 512))

    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 + self.other
        return v2


func = Model().to('cpu')


x1 = torch.rand((10, 256))

test_inputs = [x1]

# JIT_FAIL
'''
direct:
The size of tensor a (10) must match the size of tensor b (256) at non-singleton dimension 0

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., size=(10, 512)), Parameter(FakeTensor(..., size=(256, 512), requires_grad=True))), **{}):
Attempting to broadcast a dimension of length 256 at -2! Mismatching argument at index 1 had torch.Size([256, 512]); but expected shape should be broadcastable to [10, 512]

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''