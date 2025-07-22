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

    def forward(self, x):
        v1 = self.conv(x)
        v2 = v1.view(1, 8, 64 * 64)
        return v2



func = Model().to('cpu')


x = torch.randn(1, 3, 64, 64)

test_inputs = [x]

# JIT_FAIL
'''
direct:
shape '[1, 8, 4096]' is invalid for input of size 34848

jit:
Failed running call_method view(*(FakeTensor(..., size=(1, 8, s1 + 2, s2 + 2)), 1, 8, 4096), **{}):
shape '[1, 8, 4096]' is invalid for input of size (8*s1 + 16)*(s2 + 2)

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''