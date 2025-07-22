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
        self.conv = torch.nn.Conv2d(16, 16, 7, stride=1)
        self.linear1 = torch.nn.Linear((64 * 64), 4)
        self.conv2 = torch.nn.Conv2d(16, 16, 7, stride=1)
        self.linear2 = torch.nn.Linear((64 * 64), 4)

    def forward(self, x1, x2, x3, x4):
        v1 = self.conv(x1)
        v2 = v1.view((- 1), (64 * 64))
        v3 = self.linear1(v2)
        v4 = (v1 + x2)
        v5 = torch.relu(v4)
        v6 = self.conv2(v5)
        v7 = v6.view((- 1), (64 * 64))
        v8 = self.linear2(v7)
        v9 = (v8 + x3)
        v10 = torch.relu(v9)
        v11 = (v10 + x4)
        v12 = torch.relu(v11)
        return v12




func = Model().to('cuda')



x1 = torch.randn(1, 16, 64, 64)



x2 = torch.randn(1, 16, 64, 64)



x3 = torch.randn(1, 4)



x4 = torch.randn(1, 4)


test_inputs = [x1, x2, x3, x4]

# JIT_FAIL
'''
direct:
shape '[-1, 4096]' is invalid for input of size 53824

jit:
Failed running call_method view(*(FakeTensor(..., device='cuda:0', size=(1, 16, 58, 58)), -1, 4096), **{}):
shape '[-1, 4096]' is invalid for input of size 53824

from user code:
   File "<string>", line 26, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''