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



class ModelTanh(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(15, 20, kernel_size=(1, 3), padding=0, bias=False)

    def forward(self, x26):
        v27 = self.conv(x26)
        v28 = torch.tanh(v27)
        return v28




func = ModelTanh().to('cuda')



x26 = torch.randn(3, 15, 129, 1)


test_inputs = [x26]

# JIT_FAIL
'''
direct:
Calculated padded input size per channel: (129 x 1). Kernel size: (1 x 3). Kernel size can't be greater than actual input size

jit:
Failed running call_module L__self___conv(*(FakeTensor(..., device='cuda:0', size=(3, 15, 129, 1)),), **{}):
Calculated padded input size per channel: (129 x 1). Kernel size: (1 x 3). Kernel size can't be greater than actual input size

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''