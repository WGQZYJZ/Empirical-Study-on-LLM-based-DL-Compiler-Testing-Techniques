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

    def forward(self, x):
        x = x + x
        x = x + x
        y = torch.cat([x, x], dim=1)
        y = y.view(6).tanh() if y.shape != (6,) else y.view(-2).tanh()
        y = y * y
        return y



func = Model().to('cpu')


x = torch.randn(2, 2, 2)

test_inputs = [x]

# JIT_FAIL
'''
direct:
shape '[6]' is invalid for input of size 16

jit:
Failed running call_method view(*(FakeTensor(..., size=(s0, 2*s1, s2)), 6), **{}):
shape '[6]' is invalid for input of size 2*s0*s1*s2

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''