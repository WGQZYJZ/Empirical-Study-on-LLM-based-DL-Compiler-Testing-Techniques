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
        self.conv1 = nn.Conv1d(1, 64, kernel_size=(1,))
        self.batchnorm2 = nn.BatchNorm1d(64)

    def forward(self, x0):
        x1 = self.conv1(x0)
        x2 = self.batchnorm2(x1)
        x3 = torch.tanh(x1)
        return x3




func = ModelTanh().to('cuda')



x0 = torch.randn(1, 8, 256)


test_inputs = [x0]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [64, 1, 1], expected input[1, 8, 256] to have 1 channels, but got 8 channels instead

jit:
Failed running call_module L__self___conv1(*(FakeTensor(..., device='cuda:0', size=(1, 8, 256)),), **{}):
Invalid channel dimensions

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''