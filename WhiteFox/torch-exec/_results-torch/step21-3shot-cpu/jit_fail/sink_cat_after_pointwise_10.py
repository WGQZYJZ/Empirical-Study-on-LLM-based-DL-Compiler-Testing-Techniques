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
        y = x.view(x.shape[0], -1, 32, 25)
        y = y
        x = x.view(-1, 32, 3)
        z = torch.cat((x, y), dim=1)
        return z



func = Model().to('cpu')


x1 = torch.randn(16, 16, 32, 3)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
shape '[16, -1, 32, 25]' is invalid for input of size 24576

jit:
Failed running call_method view(*(FakeTensor(..., size=(s0, s1, s2, s3)), s0, -1, 32, 25), **{}):
shape '[s0, -1, 32, 25]' is invalid for input of size s0*s1*s2*s3

from user code:
   File "<string>", line 19, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''