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
        self.conv = torch.nn.Conv2d(3, 8, 3, stride=1, padding=1)

    def forward(self, x, param='default'):
        v1 = self.conv(x)
        v2 = {'other': v1 + param}
        return v2


func = Model().to('cpu')


x = torch.randn(1, 3, 64, 64)

test_inputs = [x]

# JIT_FAIL
'''
direct:
unsupported operand type(s) for +: 'Tensor' and 'str'

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., size=(1, 8, s0, 64)), 'default'), **{}):
unsupported operand type(s) for +: 'FakeTensor' and 'str'

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''