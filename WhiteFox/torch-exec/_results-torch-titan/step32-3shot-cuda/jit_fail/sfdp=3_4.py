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

    def __init__(self, in_channels, out_channels, heads=2, dropout_p=0):
        super().__init__()
        self.conv = torch.nn.Conv2d(in_channels, (heads * out_channels), 1, stride=1, padding=1)
        self.dropout = torch.nn.Dropout(dropout_p)

    def forward(self, x1, x2):
        v1 = self.conv(x1)
        (b, _, h, w) = v1.shape
        v1 = v1.reshape(b, (- 1), h, w)
        c = v1.size(1)
        v2 = x2.transpose(1, 2)
        v3 = v1.mul(v2)
        v4 = torch.nn.functional.softmax(v3, dim=2)
        v5 = self.dropout(v4)
        v6 = v5.matmul(v1)
        return v6



in_channels = 1
out_channels = 1

func = Model(in_channels, out_channels).to('cuda')



x1 = torch.randn(1, 3, 64, 64)



x2 = torch.randn(1, 64, 64)


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [2, 1, 1, 1], expected input[1, 3, 64, 64] to have 1 channels, but got 3 channels instead

jit:
Failed running call_module L__self___conv(*(FakeTensor(..., device='cuda:0', size=(1, 3, 64, 64)),), **{}):
Given groups=1, weight of size [2, 1, 1, 1], expected input[1, 3, 64, 64] to have 1 channels, but got 3 channels instead

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''