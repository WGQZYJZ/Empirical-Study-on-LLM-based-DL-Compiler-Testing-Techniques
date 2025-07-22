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
        self.conv_transpose = torch.nn.ConvTranspose2d(1, 13, 3)
        self.bn = torch.nn.BatchNorm2d(6)

    def forward(self, x1):
        v1 = self.conv_transpose(x1).clamp(min=0)
        v2 = self.bn(v1)
        v3 = (v2 * 0.7071067811865476)
        v4 = torch.erf(v3)
        v5 = (v4 + 1)
        v6 = (v2 * v5)
        return v6




func = Model().to('cuda')



x1 = torch.randn(64, 1, 32, 32)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
running_mean should contain 13 elements not 6

jit:
Failed running call_module L__self___bn(*(FakeTensor(..., device='cuda:0', size=(64, 13, 34, 34)),), **{}):
running_mean should contain 13 elements not 6

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''