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
        self.conv = torch.nn.Conv2d(3, 4, 6, stride=2, padding=2)
        self.conv_transpose = torch.nn.ConvTranspose2d(4, 4, 5, stride=1, padding=1, output_padding=1)
        self.conv_1x1 = torch.nn.Conv2d(4, 8, 1)
        self.conv_transpose_1x1 = torch.nn.ConvTranspose2d(8, 4, 1)

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = self.conv_transpose(v1)
        v3 = torch.relu(v2)
        v4 = self.conv_1x1(v3)
        v5 = torch.hardtanh(v4)
        v6 = self.conv_transpose_1x1(v5)
        return v6



func = Model().to('cpu')


x1 = torch.randn(1, 3, 128, 128)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
output padding must be smaller than either stride or dilation, but got output_padding_height: 1 output_padding_width: 1 stride_height: 1 stride_width: 1 dilation_height: 1 dilation_width: 1

jit:
AttributeError: module 'torch' has no attribute 'hardtanh'

from user code:
   File "<string>", line 27, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''