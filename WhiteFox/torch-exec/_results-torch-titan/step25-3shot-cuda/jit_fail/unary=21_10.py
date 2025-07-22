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
        self.conv1d = torch.nn.Conv1d(in_channels=2, out_channels=2, kernel_size=2, stride=1, padding=1)
        self.conv2d = torch.nn.Conv2d(in_channels=1, out_channels=3, kernel_size=2, stride=1, padding=0)

    def forward(self, x):
        x1 = self.conv2d(x)
        x2 = torch.tanh(x1)
        x3 = self.conv1d(x2)
        x4 = torch.tanh(x3)
        return x4




func = ModelTanh().to('cuda')



x = torch.randn(1, 1, 100)


test_inputs = [x]

# JIT_FAIL
'''
direct:
Calculated padded input size per channel: (1 x 100). Kernel size: (2 x 2). Kernel size can't be greater than actual input size

jit:
Failed running call_module L__self___conv2d(*(FakeTensor(..., device='cuda:0', size=(1, 1, 100)),), **{}):
Calculated padded input size per channel: (1 x 100). Kernel size: (2 x 2). Kernel size can't be greater than actual input size

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''