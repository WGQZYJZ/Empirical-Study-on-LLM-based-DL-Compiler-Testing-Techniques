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
        self.conv = torch.nn.Conv2d(3, 11, 20, stride=2, padding=10, dilation=20)
        self.tanh = torch.nn.Tanh()

    def forward(self, x2):
        v1 = self.conv(x2)
        v2 = self.tanh(v1)
        return v2




func = ModelTanh().to('cuda')



x2 = torch.randn(1, 3, 224, 224)


test_inputs = [x2]

# JIT_FAIL
'''
direct:
Calculated padded input size per channel: (244 x 244). Kernel size: (381 x 381). Kernel size can't be greater than actual input size

jit:
Failed running call_module L__self___conv(*(FakeTensor(..., device='cuda:0', size=(1, 3, 224, 224)),), **{}):
Calculated padded input size per channel: (244 x 244). Kernel size: (381 x 381). Kernel size can't be greater than actual input size

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''