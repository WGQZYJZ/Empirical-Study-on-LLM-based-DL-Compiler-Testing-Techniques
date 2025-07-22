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
        self.conv = torch.nn.Conv2d(3, 1, 7, stride=2, padding=(2, 3))
        self.conv1 = torch.nn.Conv2d(3, 10, 3, stride=2, padding=1)
        self.conv2 = torch.nn.Conv2d(10, 3, 5, stride=1, padding=2)

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = self.conv1(v1)
        v3 = self.conv2(v2)
        v4 = (v3 + 3)
        v5 = torch.clamp(v4, 0, 6)
        v6 = (v3 * v5)
        v7 = (v6 / 6)
        return v7




func = Model().to('cuda')



x1 = torch.randn(1, 3, 256, 256)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [10, 3, 3, 3], expected input[1, 1, 127, 128] to have 3 channels, but got 1 channels instead

jit:
Failed running call_module L__self___conv1(*(FakeTensor(..., device='cuda:0', size=(1, 1, 127, 128)),), **{}):
Given groups=1, weight of size [10, 3, 3, 3], expected input[1, 1, 127, 128] to have 3 channels, but got 1 channels instead

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''