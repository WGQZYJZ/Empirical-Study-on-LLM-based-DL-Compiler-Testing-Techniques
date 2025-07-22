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
        self.conv = torch.nn.Conv2d(32, 32, 3)
        self.linear = torch.nn.Linear(32, 64)
        self.transpose = torch.nn.ConvTranspose1d(32, 32, 3, stride=2)

    def forward(self, x):
        t1 = torch.abs(x)
        t2 = self.conv(t1)
        t3 = self.transpose(t2)
        t4 = self.linear(t3)
        t5 = torch.sin(t4)
        return t5




func = Model().to('cuda')



x = torch.randn(1, 32, 3)


test_inputs = [x]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [32, 32, 3, 3], expected input[1, 1, 32, 3] to have 32 channels, but got 1 channels instead

jit:
Failed running call_module L__self___conv(*(FakeTensor(..., device='cuda:0', size=(1, 32, 3)),), **{}):
Given groups=1, weight of size [32, 32, 3, 3], expected input[1, 1, 32, 3] to have 32 channels, but got 1 channels instead

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''