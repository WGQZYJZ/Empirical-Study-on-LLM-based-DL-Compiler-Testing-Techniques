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
        self.linear1 = torch.nn.Linear(2, 2)
        self.linear2 = torch.nn.Linear(2, 1)

    def forward(self, x1):
        v0 = x1.permute(0, 2, 1)
        v1 = torch.nn.functional.linear(v0, self.linear1.weight, self.linear1.bias)
        x2 = torch.nn.functional.relu(v1)
        x3 = x2.detach()
        v2 = torch.max(x3, dim=-1)[0]
        v3 = v2.unsqueeze(dim=-1)
        v2 = v2 + v3.to(v2.dtype)
        v3 = (v2 == -1).to(v2.dtype)
        v3 = x3 + v3.reshape((1, 2, 1)) - x3
        x5 = torch.max(v3, dim=-1)[0]
        v4 = x5.unsqueeze(dim=-1)
        x4 = v3 + v4.to(x5.dtype)
        x5 = (x4 == -1).to(v3.dtype)
        v1 = torch.nn.functional.linear(x5, self.linear2.weight, self.linear2.bias)
        v2 = torch.sum(torch.nn.functional.hardtanh(torch.nn.functional.tanh(v1), -1.0, 1.0))
        return v2



func = Model().to('cpu')


x1 = torch.randn(1, 2, 2)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
shape '[1, 2, 1]' is invalid for input of size 4

jit:
Failed running call_method reshape(*(FakeTensor(..., size=(1, 2, 2)), (1, 2, 1)), **{}):
shape '[1, 2, 1]' is invalid for input of size 4

from user code:
   File "<string>", line 29, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''