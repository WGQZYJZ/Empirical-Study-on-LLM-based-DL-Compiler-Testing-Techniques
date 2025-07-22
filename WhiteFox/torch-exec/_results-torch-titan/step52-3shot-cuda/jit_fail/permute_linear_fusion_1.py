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
        self.pool = torch.nn.MaxPool3d(3, stride=1, padding=0, dilation=1, return_indices=False, ceil_mode=False)
        self.conv = torch.nn.Conv2d(in_channels=1, out_channels=1, kernel_size=(1, 1), stride=(1, 1), padding=(0,), dilation=(1,))

    def forward(self, x1):
        v1 = self.pool(x1)
        v2 = v1.permute(0, 2, 3, 1)
        v3 = self.conv(v2).squeeze(3).squeeze(2)
        v4 = torch.reshape(v3, (1, 5, 2))
        return torch.mean(torch.tanh(v4), dim=(- 1))




func = Model().to('cuda')



x1 = torch.randn(1, 1, 2, 2, 3)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given input size: (1x2x2x3). Calculated output size: (1x0x0x1). Output size is too small

jit:
Failed running call_module L__self___pool(*(FakeTensor(..., device='cuda:0', size=(1, 1, 2, 2, 3)),), **{}):
Given input size: (1x2x2x3). Calculated output size: (1x0x0x1). Output size is too small

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''