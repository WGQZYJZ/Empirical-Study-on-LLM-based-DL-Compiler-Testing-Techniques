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
        self.conv_transpose = torch.nn.ConvTranspose2d(6, 1, 1, stride=2, padding=7, output_padding=7)

    def forward(self, x1):
        v1 = v2 = self.conv_transpose(x1)
        v3 = v2 * 0.125
        v5 = torch.nn.functional.one_hot(v2, num_classes=12)
        v7 = torch.nn.functional.dropout(v5, p=0.0, training=True, inplace=False)
        v6 = v3 * v7
        return v6



func = Model().to('cpu')


x1 = torch.randn(1, 6, 64, 64)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
output padding must be smaller than either stride or dilation, but got output_padding_height: 7 output_padding_width: 7 stride_height: 2 stride_width: 2 dilation_height: 1 dilation_width: 1

jit:
Failed running call_function <built-in function one_hot>(*(FakeTensor(..., size=(1, 1, 120, 120)),), **{'num_classes': 12}):
one_hot is only applicable to index tensor of type LongTensor.

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''