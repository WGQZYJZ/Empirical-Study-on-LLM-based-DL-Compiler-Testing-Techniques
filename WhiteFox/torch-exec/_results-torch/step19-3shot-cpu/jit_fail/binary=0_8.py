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
        self.conv = torch.nn.Conv2d(3, 4, 1, stride=1, padding=1)

    def forward(self, x1, other=None):
        v1 = self.conv(x1)
        v2 = other
        if other is None:
            other = torch.randn(v1.shape)
            if v1.shape[0] == 3:
                v2 = torch.randn(v1.shape)
            v3 = v2 + v1
            return v3



func = Model().to('cpu')


x1 = torch.randn(1, 3, 64, 64)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
unsupported operand type(s) for +: 'NoneType' and 'Tensor'

jit:
Failed running call_function <built-in function add>(*(None, FakeTensor(..., size=(1, 4, s1 + 2, s2 + 2))), **{}):
unsupported operand type(s) for +: 'NoneType' and 'FakeTensor'

from user code:
   File "<string>", line 26, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''