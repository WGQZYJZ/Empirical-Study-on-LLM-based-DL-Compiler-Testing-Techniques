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
        self.conv = torch.nn.Conv2d(3, 4, (1, 3), stride=(1, 1), padding=(1, 1))

    def forward(self, x):
        v1 = self.conv(x)
        v2 = [0.16, 0.9, 0.78, 0.22] - v1
        return v2



func = Model().to('cpu')


x = torch.randn(1, 3, 64, 64)

test_inputs = [x]

# JIT_FAIL
'''
direct:
unsupported operand type(s) for -: 'list' and 'Tensor'

jit:
Failed running call_function <built-in function sub>(*([0.16, 0.9, 0.78, 0.22], FakeTensor(..., size=(1, 4, 66, 64))), **{}):
unsupported operand type(s) for -: 'immutable_list' and 'FakeTensor'

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''