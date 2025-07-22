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
        y = x.view(-1)
        if torch.jit.is_scripting():
            y = y.view(5, 3)
        else:
            y = y.view(5, 3).tanh()
        y = torch.cat((y, y), dim=0)
        y = y.relu()
        y = y.clamp(min=0, max=10)
        y = y.tanh()
        x = x.tanh()
        return y + x



func = Model().to('cpu')


x = torch.randn(5, 5)

test_inputs = [x]

# JIT_FAIL
'''
direct:
shape '[5, 3]' is invalid for input of size 25

jit:
Failed running call_method view(*(FakeTensor(..., size=(s0*s1,)), 5, 3), **{}):
shape '[5, 3]' is invalid for input of size s0*s1

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''