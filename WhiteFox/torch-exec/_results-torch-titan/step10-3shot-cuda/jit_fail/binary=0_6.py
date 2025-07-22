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
        self.conv = torch.nn.Conv2d(8, 4, 1, stride=1, padding=1)

    def forward(self, x, padding=None):
        v = self.conv(x)
        if (padding == None):
            padding = torch.ones(v.shape)
        padding_ = torch.nn.functional.pad(padding, (1, 1, 1, 1))
        c = (v * padding_)
        return c




func = Model().to('cuda')



x = torch.rand(8, 4, 64, 64)


test_inputs = [x]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [4, 8, 1, 1], expected input[8, 4, 64, 64] to have 8 channels, but got 4 channels instead

jit:
Failed running call_module L__self___conv(*(FakeTensor(..., device='cuda:0', size=(8, 4, 64, 64)),), **{}):
Given groups=1, weight of size [4, 8, 1, 1], expected input[8, 4, 64, 64] to have 8 channels, but got 4 channels instead

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''