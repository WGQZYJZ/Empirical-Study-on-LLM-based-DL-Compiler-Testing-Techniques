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
        self.conv_transpose = torch.nn.ConvTranspose2d(60, 192, 5, stride=1, padding=1)
        self.conv_transpose2 = torch.nn.ConvTranspose2d(64, 40, 1, stride=16, padding=0, bias=False)

    def forward(self, x1, x2):
        v1 = self.conv_transpose(x1)
        v2 = (v1 * 0.5)
        v3 = ((v1 * v1) * v1)
        v4 = (v3 * 0.044715)
        v5 = (v1 + v4)
        v6 = (v5 * 0.7978845608028654)
        v7 = torch.tanh(v6)
        v8 = (v7 + 1)
        v9 = (v2 * v8)
        v10 = self.conv_transpose2(v9)
        return v10




func = Model().to('cuda')



x1 = torch.randn(1, 60, 24, 32)



x2 = torch.randn(1, 64, 127, 64)


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
Given transposed=1, weight of size [64, 40, 1, 1], expected input[1, 192, 26, 34] to have 64 channels, but got 192 channels instead

jit:
Failed running call_module L__self___conv_transpose2(*(FakeTensor(..., device='cuda:0', size=(1, 192, 26, 34)),), **{}):
Given transposed=1, weight of size [64, 40, 1, 1], expected input[1, 192, 26, 34] to have 64 channels, but got 192 channels instead

from user code:
   File "<string>", line 32, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''