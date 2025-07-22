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

    def __init__(self, in_channels):
        super().__init__()
        self.linear = torch.nn.Linear(in_channels, in_channels)

    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = (v1 > 0)
        v3 = (v1 * 0.01)
        v4 = torch.where(v2, v1, v3)
        return v4



in_channels = 1

func = Model(in_channels).to('cuda')



x1 = torch.randn(128, 256)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (128x256 and 1x1)

jit:
Failed running call_module L__self___linear(*(FakeTensor(..., device='cuda:0', size=(128, 256)),), **{}):
a and b must have same reduction dim, but got [128, 256] X [1, 1].

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''