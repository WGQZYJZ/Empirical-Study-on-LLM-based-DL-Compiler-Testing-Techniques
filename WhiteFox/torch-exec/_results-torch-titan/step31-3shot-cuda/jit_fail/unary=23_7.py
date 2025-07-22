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
        self.conv_transpose = torch.nn.ConvTranspose2d(64, 64, kernel_size=1, stride=1, padding=0, dilation=1, groups=8, bias=False)
        self.softmax = torch.nn.Softmax(dim=(- 1))
        self.linear = torch.nn.Linear(1, 1)
        self.conv = torch.nn.Conv2d(1, 1, 1, stride=1, padding=0, dilation=1, groups=1, bias=False)

    def forward(self, x1):
        v1 = self.conv_transpose(x1)
        v2 = self.softmax(v1)
        v3 = self.linear(v2)
        v4 = self.conv(v2)
        v5 = (v3 + v4)
        v6 = torch.tanh(v5)
        return v6




func = Model().to('cuda')



x1 = torch.randn(1, 64, 224, 224)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (14336x224 and 1x1)

jit:
Failed running call_module L__self___linear(*(FakeTensor(..., device='cuda:0', size=(1, 64, 224, 224)),), **{}):
a and b must have same reduction dim, but got [14336, 224] X [1, 1].

from user code:
   File "<string>", line 27, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''