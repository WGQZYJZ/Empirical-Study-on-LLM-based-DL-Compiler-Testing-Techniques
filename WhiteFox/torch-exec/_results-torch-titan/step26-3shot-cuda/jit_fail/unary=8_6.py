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
        self.conv_transpose1 = torch.nn.ConvTranspose2d(32, 32, 4, stride=2, output_padding=1)
        self.conv_transpose2 = torch.nn.ConvTranspose2d(16, 16, 4, stride=2, output_padding=1)

    def forward(self, x1):
        v1 = self.conv_transpose1(x1)
        v2 = (v1 + 3)
        v3 = torch.clamp(v2, min=0)
        v4 = torch.clamp(v3, max=6)
        v5 = (v1 * v4)
        v6 = (v5 / 6)
        v7 = self.conv_transpose2(v6)
        v8 = (v7 + 3)
        v9 = torch.clamp(v8, min=0)
        v10 = torch.clamp(v9, max=6)
        v11 = (v7 * v10)
        v12 = (v11 / 6)
        return v12




func = Model().to('cuda')



x1 = torch.randn(1, 32, 16, 16)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given transposed=1, weight of size [16, 16, 4, 4], expected input[1, 32, 35, 35] to have 16 channels, but got 32 channels instead

jit:
Failed running call_module L__self___conv_transpose2(*(FakeTensor(..., device='cuda:0', size=(1, 32, 35, 35)),), **{}):
Given transposed=1, weight of size [16, 16, 4, 4], expected input[1, 32, 35, 35] to have 16 channels, but got 32 channels instead

from user code:
   File "<string>", line 29, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''