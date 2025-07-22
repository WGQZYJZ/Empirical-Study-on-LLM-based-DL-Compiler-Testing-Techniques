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
        self.conv_t = torch.nn.ConvTranspose2d(64, 205, 1, padding='same', bias=True)

    def forward(self, x6):
        r1 = self.conv_t(x6)
        r2 = (r1 > 0)
        r3 = (r1 * (- 97.0))
        r4 = torch.where(r2, r1, r3)
        return torch.nn.functional.pad(torch.nn.functional.hardtanh(torch.nn.functional.glu(torch.nn.functional.hardtanh(r4, (- 96), 96), 205), (- 39), 39), (1, 2))




func = Model().to('cuda')



x6 = torch.randn(86, 64, 27, 37)


test_inputs = [x6]

# JIT_FAIL
'''
direct:
conv_transpose2d(): argument 'padding' (position 5) must be tuple of ints, but found element of type str at pos 0

jit:
Failed running call_module L__self___conv_t(*(FakeTensor(..., device='cuda:0', size=(86, 64, 27, 37)),), **{}):
conv_transpose2d(): argument 'padding' (position 5) must be tuple of ints, but found element of type str at pos 0

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''