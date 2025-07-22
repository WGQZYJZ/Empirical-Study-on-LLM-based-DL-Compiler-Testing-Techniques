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
        self.ops = torch.nn.ModuleList([torch.nn.Conv2d(7, 6, 1, stride=1, padding=0) for _ in range(5)])

    def forward(self, x1, padding1=None, padding2='torch.randn(1, 7, 64, 64)'):
        for op in self.ops:
            v1 = op(x1) + padding2
        return v1



func = Model().to('cpu')


x1 = torch.randn(1, 7, 64, 64)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
unsupported operand type(s) for +: 'Tensor' and 'str'

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., size=(1, 6, s1, s2)), 'torch.randn(1, 7, 64, 64)'), **{}):
unsupported operand type(s) for +: 'FakeTensor' and 'str'

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''