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
        self.convtranspose_out_channel = torch.nn.ConvTranspose2d(1, 4, 5, stride=1, padding=0)
        self.convtranspose_kernel_size = torch.nn.ConvTranspose2d(1, 4, [20, 120], stride=[20, 1], padding=[100, 10])
        self.convtranspose_stride = torch.nn.ConvTranspose2d(1, 4, 5, stride=[5, 3], padding=0)
        self.convtranspose_pad = torch.nn.ConvTranspose2d(1, 4, 5, stride=1, padding=[[4, 4], [14, 14]])

    def forward(self, x1):
        v1 = self.convtranspose_out_channel(x1)
        v2 = self.convtranspose_kernel_size(x1)
        v3 = self.convtranspose_stride(x1)
        v4 = self.convtranspose_pad(x1)
        v5 = (((v1 + v2) + v3) + v4)
        return v5




func = Model().to('cuda')



x1 = torch.randn(1, 1, 10, 10)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
conv_transpose2d(): argument 'padding' (position 5) must be tuple of ints, but found element of type list at pos 0

jit:
Failed running call_module L__self___convtranspose_pad(*(FakeTensor(..., device='cuda:0', size=(1, 1, 10, 10)),), **{}):
conv_transpose2d(): argument 'padding' (position 5) must be tuple of ints, but found element of type list at pos 0

from user code:
   File "<string>", line 28, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''