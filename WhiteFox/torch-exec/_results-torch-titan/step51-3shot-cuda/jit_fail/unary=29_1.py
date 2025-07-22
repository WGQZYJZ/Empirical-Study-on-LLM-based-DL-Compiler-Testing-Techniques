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

    def __init__(self, min_value=2.5, max_value=0.7):
        super().__init__()
        self.hardtanh = torch.nn.Hardtanh()
        self.conv_transpose = torch.nn.ConvTranspose2d(300, 784, 1, stride=1, padding=1)
        self.min_value = min_value
        self.max_value = max_value

    def forward(self, x3):
        v1 = self.conv_transpose(x3)
        v2 = torch.clamp_min(v1, self.min_value)
        v3 = torch.clamp_max(v2, self.max_value)
        v4 = self.hardtanh(v3)
        return v4




func = Model().to('cuda')



x3 = torch.randn(1, 300, 1, 1)


test_inputs = [x3]

# JIT_FAIL
'''
direct:
Trying to create tensor with negative dimension -1: [1, 784, -1, -1]

jit:
Failed running call_module L__self___conv_transpose(*(FakeTensor(..., device='cuda:0', size=(1, 300, 1, 1)),), **{}):
Trying to create tensor with negative dimension -1: [1, 784, -1, -1]

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''