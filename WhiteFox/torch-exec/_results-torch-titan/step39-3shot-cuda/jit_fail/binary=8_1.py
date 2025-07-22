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
        self.conv1 = torch.nn.Linear((((3 * 8) * 32) * 32), 7, bias=False)
        self.bn = torch.nn.BatchNorm1d(7)

    def forward(self, x1, x2, x3):
        v0 = x1.reshape(((- 1), (((3 * 8) * 32) * 32)))
        v1 = self.conv1(v0)
        v2 = x2.reshape(((- 1), (((3 * 8) * 32) * 32)))
        v3 = self.conv1(v2)
        v4 = torch.stack([v1, v3], dim=0)
        v5 = torch.stack([v3, v1], dim=0)
        v6 = v4.reshape(((- 1), 2, 7))
        v7 = self.bn(v6)
        v8 = torch.cat([v7, v5], dim=1)
        v9 = v8.reshape(((- 1), 14, 7))
        return v9




func = Model().to('cuda')



x1 = torch.randn(1, 3, 64, 64)



x2 = torch.randn(1, 3, 64, 64)



x3 = torch.randn(1, 3, 64, 64)


test_inputs = [x1, x2, x3]

# JIT_FAIL
'''
direct:
shape '[-1, 24576]' is invalid for input of size 12288

jit:
Failed running call_method reshape(*(FakeTensor(..., device='cuda:0', size=(1, 3, 64, 64)), (-1, 24576)), **{}):
shape '[-1, 24576]' is invalid for input of size 12288

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''