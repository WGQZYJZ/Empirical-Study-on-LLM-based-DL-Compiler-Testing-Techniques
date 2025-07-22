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
        self.conv_t = torch.nn.ConvTranspose2d(8, 4, 3, stride=1, padding='same', output_padding=(0, 1), bias=False)

    def forward(self, x3):
        x4 = self.conv_t(x3)
        x5 = (x4 > 0)
        x6 = (x4 * 1.586)
        x7 = torch.where(x5, x4, x6)
        return x7




func = Model().to('cuda')



x3 = torch.randn(6, 8, 14, 14)


test_inputs = [x3]

# JIT_FAIL
'''
direct:
conv_transpose2d(): argument 'padding' (position 5) must be tuple of ints, but found element of type str at pos 0

jit:
Failed running call_module L__self___conv_t(*(FakeTensor(..., device='cuda:0', size=(6, 8, 14, 14)),), **{}):
conv_transpose2d(): argument 'padding' (position 5) must be tuple of ints, but found element of type str at pos 0

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''