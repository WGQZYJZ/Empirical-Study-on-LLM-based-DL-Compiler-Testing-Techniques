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
        self.conv = torch.nn.Conv2d(16, 24, 1, stride=1, padding=1)
        self.linear = torch.nn.Linear(16, 1)

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.sigmoid(v1)
        v3 = self.linear(x1)
        return v3




func = Model().to('cuda')



x1 = torch.randn(1, 2, 3, 4)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [24, 16, 1, 1], expected input[1, 2, 3, 4] to have 16 channels, but got 2 channels instead

jit:
Failed running call_module L__self___conv(*(FakeTensor(..., device='cuda:0', size=(1, 2, 3, 4)),), **{}):
Given groups=1, weight of size [24, 16, 1, 1], expected input[1, 2, 3, 4] to have 16 channels, but got 2 channels instead

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''