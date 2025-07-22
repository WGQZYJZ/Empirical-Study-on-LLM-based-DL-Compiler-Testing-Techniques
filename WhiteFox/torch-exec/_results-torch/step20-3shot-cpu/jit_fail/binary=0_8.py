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
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x1, other=1, padding1=None, padding2=None, padding3=None):
        v1 = self.conv(x1)
        if padding1 == None:
            padding1 = torch.randn(v1.shape)
        if padding2 == None and padding3 == None:
            padding2 = torch.randn(v1.shape) * padding3
        v2 = v1 + other
        return v2



func = Model().to('cpu')


x1 = torch.randn(1, 3, 64, 64)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
unsupported operand type(s) for *: 'Tensor' and 'NoneType'

jit:
Failed running call_function <built-in function mul>(*(FakeTensor(..., size=(1, 8, s1 + 2, s2 + 2)), None), **{}):
unsupported operand type(s) for *: 'FakeTensor' and 'NoneType'

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''