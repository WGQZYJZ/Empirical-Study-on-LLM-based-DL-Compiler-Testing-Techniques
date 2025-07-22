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
        self.conv = torch.nn.Conv2d(32, 16, 3, stride=2, padding=1)

    def forward(self, x):
        v1 = self.conv(x)
        v2 = (1 + v1)
        v3 = torch.tanh(v2)
        v4 = (1 + 1)
        v5 = (v3 + v4)
        v6 = (v5 * v1)
        v7 = v6.view(16)
        v8 = (v7 - v7)
        v9 = torch.sigmoid(v8)
        return v9




func = Model().to('cuda')



x = torch.randn(1, 32, 28, 28)


test_inputs = [x]

# JIT_FAIL
'''
direct:
shape '[16]' is invalid for input of size 3136

jit:
Failed running call_method view(*(FakeTensor(..., device='cuda:0', size=(1, 16, 14, 14)), 16), **{}):
shape '[16]' is invalid for input of size 3136

from user code:
   File "<string>", line 28, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''