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
        self.conv = torch.nn.ConvTranspose2d(35, 32, 3, stride=1, padding=2)
        self.conv = torch.nn.ConvTranspose2d(32, 96, 3, stride=1, padding=2)

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.tanh(v1)
        return v2




func = Model().to('cuda')



x1 = torch.randn(1, 35, 10, 10)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given transposed=1, weight of size [32, 96, 3, 3], expected input[1, 35, 10, 10] to have 32 channels, but got 35 channels instead

jit:
Failed running call_module L__self___conv(*(FakeTensor(..., device='cuda:0', size=(1, 35, 10, 10)),), **{}):
Given transposed=1, weight of size [32, 96, 3, 3], expected input[1, 35, 10, 10] to have 32 channels, but got 35 channels instead

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''