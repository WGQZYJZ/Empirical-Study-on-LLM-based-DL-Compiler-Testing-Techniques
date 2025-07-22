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

    def __init__(self, in_c, out_c, kernel_size=3, stride=2, padding=1):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(in_c, out_c, kernel_size, stride=stride, padding=padding)

    def forward(self, x, negative_slope):
        v1 = self.conv1(x)
        v3 = (v1 > 0)
        v4 = (v1 * negative_slope)
        v5 = torch.where(v3, v1, v4)
        return v5



in_c = 1
out_c = 1

func = Model(in_c, out_c).to('cuda')



x1 = torch.randn(1, 8, 256, 256)

x = 1

test_inputs = [x1, x]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [1, 1, 3, 3], expected input[1, 8, 256, 256] to have 1 channels, but got 8 channels instead

jit:
Failed running call_module L__self___conv1(*(FakeTensor(..., device='cuda:0', size=(1, 8, 256, 256)),), **{}):
Given groups=1, weight of size [1, 1, 3, 3], expected input[1, 8, 256, 256] to have 1 channels, but got 8 channels instead

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''