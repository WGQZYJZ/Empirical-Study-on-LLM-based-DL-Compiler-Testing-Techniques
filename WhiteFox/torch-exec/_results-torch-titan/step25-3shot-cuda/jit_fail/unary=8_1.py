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
        self.conv_transpose1 = torch.nn.ConvTranspose2d(18, 18, 5, stride=3, dilation=15, output_padding=1, padding=0)
        self.conv_transpose2 = torch.nn.ConvTranspose2d(1, 32, 5, stride=3, dilation=7, output_padding=3, padding=5)
        self.conv_transpose3 = torch.nn.ConvTranspose2d(32, 22, 5, stride=3, dilation=19, output_padding=2, padding=4)

    def forward(self, x1):
        v1 = self.conv_transpose1(x1)
        v2 = self.conv_transpose2(v1)
        v3 = self.conv_transpose3(v2)
        v4 = (v3 + 3)
        v5 = torch.clamp(v4, min=0)
        v6 = torch.clamp(v5, max=6)
        v7 = (v3 * v6)
        v8 = (v7 / 6)
        return v8




func = Model().to('cuda')



x1 = torch.randn(1, 18, 42, 39)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given transposed=1, weight of size [1, 32, 5, 5], expected input[1, 18, 185, 176] to have 1 channels, but got 18 channels instead

jit:
Failed running call_module L__self___conv_transpose2(*(FakeTensor(..., device='cuda:0', size=(1, 18, 185, 176)),), **{}):
Given transposed=1, weight of size [1, 32, 5, 5], expected input[1, 18, 185, 176] to have 1 channels, but got 18 channels instead

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''