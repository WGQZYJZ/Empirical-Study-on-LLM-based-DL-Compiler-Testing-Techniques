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
        self.conv2d = torch.nn.Conv2d(1, 4, 1, stride=1, padding=0)
        self.conv_transpose = torch.nn.ConvTranspose2d(32, 32, (2, 1), stride=(2, 1), padding=(0, 0))

    def forward(self, x1):
        v1 = self.conv2d(x1)
        v2 = (v1 * 0.5)
        v3 = (v1 * 0.7071067811865476)
        v4 = torch.erf(v3)
        v5 = (v4 + 1)
        v6 = (v2 * v5)
        v7 = self.conv_transpose(v6)
        return v7




func = Model().to('cuda')



x1 = torch.randn(1, 32, 28, 28)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [4, 1, 1, 1], expected input[1, 32, 28, 28] to have 1 channels, but got 32 channels instead

jit:
Failed running call_module L__self___conv2d(*(FakeTensor(..., device='cuda:0', size=(1, 32, 28, 28)),), **{}):
Given groups=1, weight of size [4, 1, 1, 1], expected input[1, 32, 28, 28] to have 1 channels, but got 32 channels instead

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''