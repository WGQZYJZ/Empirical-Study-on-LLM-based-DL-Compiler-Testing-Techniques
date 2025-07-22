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
        self.conv = torch.nn.Conv2d(512, 56, 1, stride=2, padding=0)
        self.linear = torch.nn.Linear(56, 10)

    def forward(self, x):
        y = x.view(-1, 512 * 8 * 8)
        v1 = self.conv(y)
        v2 = self.linear(v1.view(-1, 56))
        v3 = v2 - 5
        return v3



func = Model().to('cpu')


x = torch.randn(1, 512, 4, 4)

test_inputs = [x]

# JIT_FAIL
'''
direct:
shape '[-1, 32768]' is invalid for input of size 8192

jit:
Failed running call_method view(*(FakeTensor(..., size=(1, 512, 4, 4)), -1, 32768), **{}):
shape '[-1, 32768]' is invalid for input of size 8192

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''