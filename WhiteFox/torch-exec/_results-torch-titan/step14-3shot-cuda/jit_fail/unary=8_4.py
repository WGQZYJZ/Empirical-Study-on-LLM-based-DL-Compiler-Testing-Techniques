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
        self.conv_transpose = torch.nn.ConvTranspose2d(64, 128, 1, stride=2, padding=0, dilation=1, output_padding=0)
        self.fc = torch.nn.Linear(768, 1024, bias=True)

    def forward(self, x1):
        v1 = self.conv_transpose(x1)
        v2 = v1.flatten(1)
        v3 = self.fc(v2)
        v4 = (v3 + 3)
        v5 = torch.clamp(v4, min=0)
        v6 = torch.clamp(v5, max=6)
        v7 = (v3 * v6)
        v8 = (v7 / 6)
        return v8




func = Model().to('cuda')



x1 = torch.randn(1, 64, 64, 64)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (1x2064512 and 768x1024)

jit:
Failed running call_module L__self___fc(*(FakeTensor(..., device='cuda:0', size=(1, 2064512)),), **{}):
a and b must have same reduction dim, but got [1, 2064512] X [768, 1024].

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''