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
        self.conv1 = torch.nn.Conv2d(4, 4, 3, stride=2, padding=1)
        self.conv2 = torch.nn.Conv2d(8, 8, 3, stride=1, padding=0)

    def forward(self, x):
        v1 = self.conv1(x)
        v2 = (v1 > 0)
        v3 = (v1 * 0.2)
        v4 = torch.where(v2, v1, v3)
        v5 = self.conv2(v4)
        v6 = (v5 > 0)
        v7 = (v5 * 0.1)
        v8 = torch.where(v6, v5, v7)
        return v8




func = Model().to('cuda')



x1 = torch.randn(1, 4, 48, 48)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [8, 8, 3, 3], expected input[1, 4, 24, 24] to have 8 channels, but got 4 channels instead

jit:
Failed running call_module L__self___conv2(*(FakeTensor(..., device='cuda:0', size=(1, 4, 24, 24)),), **{}):
Given groups=1, weight of size [8, 8, 3, 3], expected input[1, 4, 24, 24] to have 8 channels, but got 4 channels instead

from user code:
   File "<string>", line 27, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''