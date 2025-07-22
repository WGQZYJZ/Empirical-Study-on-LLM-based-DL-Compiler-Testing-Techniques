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

class WeightedCat(torch.nn.Module):

    def __init__(self, in_ch, out_ch, kernel_size, stride=-1):
        super().__init__()
        if stride == -1:
            self.conv = torch.nn.Conv2d(in_ch, out_ch, kernel_size, stride, bias=False)
        else:
            self.conv = torch.nn.ConvTranspose2d(in_ch, out_ch, kernel_size, stride, bias=False)

    def forward(self, inp, mat1, mat2):
        v1 = self.conv(inp)
        v2 = torch.addmm(inp, v1, mat1, beta=0.5, alpha=0.5)
        v3 = torch.addmm(v2, mat2, mat1)
        return v3


in_ch = 1
out_ch = 1
kernel_size = 1
func = WeightedCat(3, 8, 3, stride=2).to('cpu')


x1 = torch.randn(1, 3, 32, 32)

x2 = torch.randn(8, 3, 3, 3)

x3 = torch.randn(8, 3, 3, 3)

test_inputs = [x1, x2, x3]

# JIT_FAIL
'''
direct:
mat1 must be a matrix, got 4-D tensor

jit:
Failed running call_function <built-in method addmm of type object at 0x71ddb4396ec0>(*(FakeTensor(..., size=(1, 3, 32, 32)), FakeTensor(..., size=(1, 8, 65, 65)), FakeTensor(..., size=(8, 3, 3, 3))), **{'beta': 0.5, 'alpha': 0.5}):
a must be 2D

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''