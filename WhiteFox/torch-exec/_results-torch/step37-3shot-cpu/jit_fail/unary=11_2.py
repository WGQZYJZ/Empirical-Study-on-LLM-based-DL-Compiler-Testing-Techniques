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

    def forward(self, x1):
        v1 = (x1 + 3).transpose(0, 1).view(32, 64, 16)
        v2 = v1 - 3
        v3 = torch.clamp_min(v2, 0)
        v4 = torch.clamp_max(v3, 6)
        v5 = v4 / 6
        return x1



func = Model().to('cpu')


x1 = torch.randn(1, 64, 24)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
shape '[32, 64, 16]' is invalid for input of size 1536

jit:
Failed running call_method view(*(FakeTensor(..., size=(64, 1, 24)), 32, 64, 16), **{}):
shape '[32, 64, 16]' is invalid for input of size 1536

from user code:
   File "<string>", line 19, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''