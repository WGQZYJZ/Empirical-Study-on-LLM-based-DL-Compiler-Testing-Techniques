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
        self.conv1 = torch.nn.Conv2d(4, 2, 1, dilation=2, padding=2)
        self.conv2a = torch.nn.Conv2d(2, 1, 3, stride=1, padding=1)
        self.conv2b = torch.nn.Conv2d(2, 1, 1, stride=1, padding=0)

    def forward(self, x):
        v1 = self.conv1(x)
        v2a = self.conv2a(v1[:, 0:1, :, :])
        v2b = self.conv2b(v1[:, 1:2, :, :])
        v3 = torch.tanh((v2a + v2b))
        return v3




func = ModelTanh().to('cuda')



x = torch.randn(1, 4, 3, 3)


test_inputs = [x]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [1, 2, 3, 3], expected input[1, 1, 7, 7] to have 2 channels, but got 1 channels instead

jit:
Failed running call_module L__self___conv2a(*(FakeTensor(..., device='cuda:0', size=(1, 1, 7, 7)),), **{}):
Given groups=1, weight of size [1, 2, 3, 3], expected input[1, 1, 7, 7] to have 2 channels, but got 1 channels instead

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''