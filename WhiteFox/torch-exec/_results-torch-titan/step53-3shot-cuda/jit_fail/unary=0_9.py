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
        self.conv = torch.nn.Conv2d(4, 1, 1, stride=1, padding=6)

    def forward(self, x4):
        v1 = self.conv(x4)
        v2 = torch.tanh(v1)
        return v1




func = Model().to('cuda')



x4 = torch.randn(4, 16, 1, 1)


test_inputs = [x4]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [1, 4, 1, 1], expected input[4, 16, 1, 1] to have 4 channels, but got 16 channels instead

jit:
Failed running call_module L__self___conv(*(FakeTensor(..., device='cuda:0', size=(4, 16, 1, 1)),), **{}):
Given groups=1, weight of size [1, 4, 1, 1], expected input[4, 16, 1, 1] to have 4 channels, but got 16 channels instead

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''