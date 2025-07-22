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
        self.conv = torch.nn.Conv2d(64, 32, 3, padding=1)

    def forward(self, x1, x2, x3, x4, x5, x6):
        v1 = self.conv(torch.cat([x6, x4, x3, x2, x1], 1))
        v2 = torch.sigmoid(v1)
        return v2




func = Model().to('cuda')



x1 = torch.randn(1, 64, 224, 224)



x2 = torch.randn(1, 64, 224, 224)



x3 = torch.randn(1, 64, 224, 224)



x4 = torch.randn(1, 64, 224, 224)



x5 = torch.randn(1, 64, 224, 224)



x6 = torch.randn(1, 64, 224, 224)


test_inputs = [x1, x2, x3, x4, x5, x6]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [32, 64, 3, 3], expected input[1, 320, 224, 224] to have 64 channels, but got 320 channels instead

jit:
Failed running call_module L__self___conv(*(FakeTensor(..., device='cuda:0', size=(1, 320, 224, 224)),), **{}):
Given groups=1, weight of size [32, 64, 3, 3], expected input[1, 320, 224, 224] to have 64 channels, but got 320 channels instead

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''