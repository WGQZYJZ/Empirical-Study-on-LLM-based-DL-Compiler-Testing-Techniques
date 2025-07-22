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
        self.conv_transpose = torch.nn.ConvTranspose3d(3, 64, 3, stride=1, padding=1, output_padding=1)

    def forward(self, x1):
        v1 = self.conv_transpose(x1)
        v2 = v1 * 0.5
        v3 = v4 + 1
        v6 = v2 * v5
        return v6



func = Model().to('cpu')


x1 = torch.randn(1, 3, 60, 30, 50)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
output padding must be smaller than either stride or dilation, but got output_padding_depth: 1 output_padding_height: 1 output_padding_width: 1 stride_depth: 1 stride_height: 1 stride_width: 1 dilation_depth: 1 dilation_height: 1 dilation_width: 1

jit:
NameError: name 'v4' is not defined

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''