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

    def __init__(self, min_value=(- 0.5), max_value=1):
        super().__init__()
        self.max_pool1d = torch.nn.MaxPool1d(5, stride=2, padding=1, dilation=3)
        self.conv_transpose = torch.nn.ConvTranspose2d(1, 3, 1, stride=2, padding=2)
        self.min_value = min_value
        self.max_value = max_value

    def forward(self, x1):
        v1 = self.conv_transpose(x1)
        v2 = torch.clamp_min(v1, self.min_value)
        v3 = torch.clamp_max(v2, self.max_value)
        v4 = self.max_pool1d(v3)
        return v4




func = Model().to('cuda')



x1 = torch.randn(1, 1, 5, 2)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Trying to create tensor with negative dimension -1: [1, 3, 5, -1]

jit:
Failed running call_module L__self___conv_transpose(*(FakeTensor(..., device='cuda:0', size=(1, 1, 5, 2)),), **{}):
Trying to create tensor with negative dimension -1: [1, 3, 5, -1]

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''