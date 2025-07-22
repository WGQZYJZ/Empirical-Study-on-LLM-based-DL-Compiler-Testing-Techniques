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
        self.conv_t = torch.nn.ConvTranspose2d(56, 76, 7, stride=3, padding=1, output_padding=5, bias=False, dilation=1)

    def forward(self, hidden):
        out = self.conv_t(hidden)
        mask = out > 0
        mul = out * 0.03
        out = torch.where(mask, out, mul)
        out = torch.nn.functional.adaptive_max_pool2d(out, (55, 139))
        out = torch.nn.functional.layer_norm(out, normalized_shape=[1, 1, 82, 171], weight=None, bias=None, eps=1e-05)
        return torch.nn.functional.layer_norm(out, normalized_shape=[1, 1, 82, 171], weight=None, bias=None, eps=1e-05)



func = Model().to('cpu')


hidden = torch.randn(24, 56, 70, 104)

test_inputs = [hidden]

# JIT_FAIL
'''
direct:
output padding must be smaller than either stride or dilation, but got output_padding_height: 5 output_padding_width: 5 stride_height: 3 stride_width: 3 dilation_height: 1 dilation_width: 1

jit:
Failed running call_function <function layer_norm at 0x7e2eee371040>(*(FakeTensor(..., size=(24, 76, 55, 139)),), **{'normalized_shape': [1, 1, 82, 171], 'weight': None, 'bias': None, 'eps': 1e-05}):
Given normalized_shape=[1, 1, 82, 171], expected input with shape [1, 1, 82, 171], but got input of size torch.Size([24, 76, 55, 139])

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''