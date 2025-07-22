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

    def __init__(self, in_channels, out_channels, key_dim, value_dim):
        super().__init__()
        self.in_channels = in_channels
        self.out_channels = out_channels
        self.key_dim = key_dim
        self.value_dim = value_dim
        self.scale_factor = math.sqrt(key_dim)
        self.query_conv = torch.nn.Conv2d(in_channels, key_dim, 1)
        self.key_conv = torch.nn.Conv2d(in_channels, key_dim, 1)
        self.value_conv = torch.nn.Conv2d(in_channels, value_dim, 1)

    def forward(self, x1):
        __p9 = print
        __p9('query.shape = {}'.format('x1.shape'))
        v1 = self.query_conv(x1)
        __p9('key.shape = {}'.format('x1.shape'))
        v2 = self.key_conv(x1)
        __p9('value.shape = {}'.format('x1.shape'))
        v3 = self.value_conv(x1)
        qk = torch.matmul(v1, v2.transpose((- 2), (- 1)))
        scaled_qk = qk.div(self.scale_factor)
        softmax_qk = scaled_qk.softmax(dim=(- 1))
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        return dropout_qk.matmul(v3)



in_channels = 1
out_channels = 1
key_dim = 1
value_dim = 1

func = Model(in_channels, out_channels, key_dim, value_dim).to('cuda')



x1 = torch.randn(1, 3, 64, 64)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [1, 1, 1, 1], expected input[1, 3, 64, 64] to have 1 channels, but got 3 channels instead

jit:
Failed running call_module L__self___query_conv(*(FakeTensor(..., device='cuda:0', size=(1, 3, 64, 64)),), **{}):
Given groups=1, weight of size [1, 1, 1, 1], expected input[1, 3, 64, 64] to have 1 channels, but got 3 channels instead

from user code:
   File "<string>", line 31, in <resume in forward>


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''