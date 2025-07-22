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

    def __init__(self, min_value=2.0, max_value=0.7):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose2d(10, 16, 1, stride=1)
        self.min_value = min_value
        self.max_value = max_value

    def forward(self, x1):
        v1 = self.conv_transpose(x1)
        v2 = torch.clamp_min(v1, self.min_value)
        v3 = torch.clamp_max(v2, self.max_value)
        return v3




func = Model().to('cuda')



x1 = torch.randn(1, 10, 64)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given transposed=1, weight of size [10, 16, 1, 1], expected input[1, 1, 10, 64] to have 10 channels, but got 1 channels instead

jit:
Failed running call_module L__self___conv_transpose(*(FakeTensor(..., device='cuda:0', size=(1, 10, 64)),), **{}):
Given transposed=1, weight of size [10, 16, 1, 1], expected input[1, 1, 10, 64] to have 10 channels, but got 1 channels instead

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''