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
        self.conv = torch.nn.ConvTranspose2d(3, 8, 3, stride=2, padding=1)
        self.relu = torch.nn.ReLU()

    def forward(self, x):
        v1 = self.conv(x)
        v2 = (v1 * 0.5)
        v3 = self.relu((v2 + self.conv(v1)))
        v4 = (v1 * 0.7071067811865476)
        v5 = (v1 * 0.044715)
        v6 = (v3 * 0.7978845608028654)
        v7 = (v3 + self.conv(((v1 * v5) * v4)))
        v8 = torch.tanh(v7)
        v9 = (v2 * v8)
        return v9



func = Model().to('cuda')



x = torch.randn(1, 3, 64, 64)


test_inputs = [x]

# JIT_FAIL
'''
direct:
Given transposed=1, weight of size [3, 8, 3, 3], expected input[1, 8, 127, 127] to have 3 channels, but got 8 channels instead

jit:
Failed running call_module L__self___conv(*(FakeTensor(..., device='cuda:0', size=(1, 8, 127, 127)),), **{}):
Given transposed=1, weight of size [3, 8, 3, 3], expected input[1, 8, 127, 127] to have 3 channels, but got 8 channels instead

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''