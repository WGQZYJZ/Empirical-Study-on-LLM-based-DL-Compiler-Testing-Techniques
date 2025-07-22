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
        self.conv_transpose = torch.nn.ConvTranspose2d(3, 6, 3, stride=(1, 2), padding={'str_dict': 1, 'int_list': 1, 'float_number': 1}, dilation=(1, 2), groups=1, bias=False)

    def forward(self, x1):
        v1 = self.conv_transpose(x1)
        v2 = (v1 * 0.5)
        v3 = ((v1 * v1) * v1)
        v4 = (v3 * 0.044715)
        v5 = (v1 + v4)
        v6 = (v5 * 0.7978845608028654)
        v7 = torch.tanh(v6)
        v8 = (v7 + 1)
        v9 = (v2 * v8)
        return v9




func = Model().to('cuda')



x1 = torch.randn(1, 3, 23, 11)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
conv_transpose2d(): argument 'padding' (position 5) must be tuple of ints, but found element of type str at pos 0

jit:
Failed running call_module L__self___conv_transpose(*(FakeTensor(..., device='cuda:0', size=(1, 3, 23, 11)),), **{}):
conv_transpose2d(): argument 'padding' (position 5) must be tuple of ints, but found element of type str at pos 0

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''