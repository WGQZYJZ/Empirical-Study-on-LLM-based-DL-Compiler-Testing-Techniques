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
        super(Model, self).__init__()
        self.conv_t = torch.nn.ConvTranspose2d(81, 79, 3, stride=1, padding=0, bias=True)

    def forward(self, x12):
        l1 = self.conv_t(x12)
        s1 = torch.nn.functional.interpolate(l1, scale_factor=(0.226,), mode='nearest', align_corners=None)
        return s1



func = Model().to('cpu')


x12 = torch.randn(52, 81, 52, 67)

test_inputs = [x12]

# JIT_FAIL
'''
direct:
Input and scale_factor must have the same number of spatial dimensions, but got input with spatial dimensions of [54, 69] and scale_factor of shape (0.226,). Please provide input tensor in (N, C, d1, d2, ...,dK) format and scale_factor in (s1, s2, ...,sK) format.

jit:
Failed running call_function <function interpolate at 0x73e85b25b0d0>(*(FakeTensor(..., size=(52, 79, 54, 69)),), **{'scale_factor': (0.226,), 'mode': 'nearest', 'align_corners': None}):
Input and scale_factor must have the same number of spatial dimensions, but got input with spatial dimensions of [54, 69] and scale_factor of shape (0.226,). Please provide input tensor in (N, C, d1, d2, ...,dK) format and scale_factor in (s1, s2, ...,sK) format.

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''