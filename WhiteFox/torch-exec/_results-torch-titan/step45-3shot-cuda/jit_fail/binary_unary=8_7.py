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
        self.conv = torch.nn.Conv2d(40, 10, 1)
        self.convt = torch.nn.ConvTranspose2d(10, 40, 1)

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = self.conv(x1)
        v3 = self.convt(v1)
        v4 = self.convt(v2)
        v5 = (v3 + v4)
        v6 = torch.relu(v5)
        return v6




func = Model().to('cuda')



x1 = torch.randn(1, 3, 320, 640)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [10, 40, 1, 1], expected input[1, 3, 320, 640] to have 40 channels, but got 3 channels instead

jit:
Failed running call_module L__self___conv(*(FakeTensor(..., device='cuda:0', size=(1, 3, 320, 640)),), **{}):
Given groups=1, weight of size [10, 40, 1, 1], expected input[1, 3, 320, 640] to have 40 channels, but got 3 channels instead

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''