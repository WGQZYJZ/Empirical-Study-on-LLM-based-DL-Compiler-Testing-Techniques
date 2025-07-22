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
        self.conv = torch.nn.Conv2d(2, 6, 4, stride=1, padding=0)
        self.conv2 = torch.nn.Conv2d(6, 1, 1, stride=1, padding=0)
        self.max_pool = torch.nn.MaxPool2d(1, stride=1, padding=0)

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = (v1 * 0.5)
        v3 = (v1 * 0.7071067811865476)
        v4 = torch.erf(v3)
        v5 = (v4 + 1)
        v6 = (v2 * v5)
        v7 = self.conv2(v6)
        v8 = self.max_pool(v7)
        v9 = v8.view((- 1), 12)
        return v9




func = Model().to('cuda')



x1 = torch.randn(1, 2, 19, 47)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
shape '[-1, 12]' is invalid for input of size 704

jit:
Failed running call_method view(*(FakeTensor(..., device='cuda:0', size=(1, 1, 16, 44)), -1, 12), **{}):
shape '[-1, 12]' is invalid for input of size 704

from user code:
   File "<string>", line 32, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''