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
        self.linear = torch.nn.Linear(2, 1)

    def forward(self, x1):
        x = torch.transpose(x1, 2, 3)
        x = x.reshape((- 1), 300)
        x = self.linear(x)
        v2 = (x * 0.5)
        v4 = torch.erf((x * 0.7071067811865476))
        v5 = (v4 + 1)
        y = (v2 * v5)
        y = torch.transpose(y.reshape(1, 4, (- 1), 300), 2, 3)
        return y



func = Model().to('cuda')



x1 = torch.randn(1, 4, 300, 2)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (8x300 and 2x1)

jit:
Failed running call_module L__self___linear(*(FakeTensor(..., device='cuda:0', size=(8, 300)),), **{}):
a and b must have same reduction dim, but got [8, 300] X [2, 1].

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''