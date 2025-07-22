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
        self.conv_transpose = torch.nn.ConvTranspose3d(6, 3, (7, 7, 3), stride=(3, 3, 3), padding=(2, 2, 2))
        self.conv = torch.nn.Conv3d(4, 8, kernel_size=(3, 3, 2), stride=(2, 2, 1), padding=(1, 1, 1))
        self.pool = torch.nn.MaxPool3d(5, stride=1)

    def forward(self, x1):
        v1 = self.conv_transpose(x1)
        v2 = torch.tanh(v1)
        v3 = self.conv(v2)
        v4 = torch.tanh(v3)
        v5 = v4.contiguous()
        v6 = self.pool(v5)
        return v6




func = Model().to('cuda')



x1 = torch.randn(1, 6, 64, 32, 64)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [8, 4, 3, 3, 2], expected input[1, 3, 192, 96, 188] to have 4 channels, but got 3 channels instead

jit:
Failed running call_module L__self___conv(*(FakeTensor(..., device='cuda:0', size=(1, 3, 192, 96, 188)),), **{}):
Given groups=1, weight of size [8, 4, 3, 3, 2], expected input[1, 3, 192, 96, 188] to have 4 channels, but got 3 channels instead

from user code:
   File "<string>", line 26, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''