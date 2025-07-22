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

    def __init__(self, min_value=0, max_value=0):
        super().__init__()
        self.conv_transpose2d_1 = torch.nn.ConvTranspose2d(6, 3, 4, stride=4, padding=0, bias=False)
        self.conv2d_1 = torch.nn.Conv2d(2, 5, 2, stride=3, padding=2, bias=False)
        self.min_value = min_value
        self.max_value = max_value

    def forward(self, x3):
        v2 = self.conv_transpose2d_1(x3)
        v1 = self.conv2d_1(v2)
        v3 = torch.clamp_min(v1, self.min_value)
        v4 = torch.clamp_max(v3, self.max_value)
        return v4




func = Model().to('cuda')



x3 = torch.randn(1, 6, 5, 1)


test_inputs = [x3]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [5, 2, 2, 2], expected input[1, 3, 20, 4] to have 2 channels, but got 3 channels instead

jit:
Failed running call_module L__self___conv2d_1(*(FakeTensor(..., device='cuda:0', size=(1, 3, 20, 4)),), **{}):
Given groups=1, weight of size [5, 2, 2, 2], expected input[1, 3, 20, 4] to have 2 channels, but got 3 channels instead

from user code:
   File "<string>", line 26, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''