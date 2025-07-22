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

    def __init__(self, min_value=(- 0.765), max_value=(+ 1.169)):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose2d(3, 6, 1, stride=1, padding=992)
        self.min_value = min_value
        self.max_value = max_value

    def forward(self, x1):
        v1 = self.conv_transpose(x1)
        v2 = torch.clamp_min(v1, self.min_value)
        v3 = torch.clamp_max(v2, self.max_value)
        return v3




func = Model().to('cuda')



x1 = torch.randn(1, 3, 52, 63)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Trying to create tensor with negative dimension -1932: [1, 6, -1932, -1921]

jit:
Failed running call_module L__self___conv_transpose(*(FakeTensor(..., device='cuda:0', size=(1, 3, 52, 63)),), **{}):
Trying to create tensor with negative dimension -1932: [1, 6, -1932, -1921]

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''