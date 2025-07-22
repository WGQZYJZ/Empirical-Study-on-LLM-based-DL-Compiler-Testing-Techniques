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
        v3 = torch.sum(self.linear1(x1), dim=1)
        x2 = torch.tanh(v3)
        v1 = x2 * x2
        v2 = torch.squeeze(self.linear2(v1), dim=1)
        v4 = torch.abs(v2)
        return v4



func = Model().to('cpu')


x1 = torch.randn(2, 2)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Dimension out of range (expected to be in range of [-1, 0], but got 1)

jit:
Failed running call_function <built-in method squeeze of type object at 0x7fb823b96ec0>(*(FakeTensor(..., size=(1,)),), **{'dim': 1}):
Dimension out of range (expected to be in range of [-1, 0], but got 1)

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''