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
        self.convt1 = torch.nn.ConvTranspose2d(3, 8, 3, stride=1, padding=1)
        self.convt2 = torch.nn.ConvTranspose2d(4, 6, 3, stride=1, padding=1)

    def forward(self, x):
        v1 = self.convt1(x)
        v2 = self.convt2((v1 / 0.7978845608028654))
        v3 = (v1 + torch.tanh((v2 / 0.044715)))
        v4 = (v3 * 0.5)
        v5 = self.convt2(v4)
        v6 = self.convt1((v2 * v2))
        v7 = ((v5 * torch.tanh(v6)) + 0.44715)
        v8 = self.convt2(v7)
        v9 = self.convt2(v8)
        v10 = (v9 * v9)
        v11 = (v8 * v10)
        v12 = (v8 + v11)
        return v12



func = Model().to('cuda')



x = torch.randn(1, 3, 64, 64)


test_inputs = [x]

# JIT_FAIL
'''
direct:
Given transposed=1, weight of size [4, 6, 3, 3], expected input[1, 8, 64, 64] to have 4 channels, but got 8 channels instead

jit:
Failed running call_module L__self___convt2(*(FakeTensor(..., device='cuda:0', size=(1, 8, 64, 64)),), **{}):
Given transposed=1, weight of size [4, 6, 3, 3], expected input[1, 8, 64, 64] to have 4 channels, but got 8 channels instead

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''