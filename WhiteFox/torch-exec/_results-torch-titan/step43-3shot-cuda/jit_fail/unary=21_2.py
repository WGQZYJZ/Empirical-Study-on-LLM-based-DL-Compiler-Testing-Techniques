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
        self.conv1 = torch.nn.Conv2d(1, 6, 1, 1, padding=2)
        self.conv2 = torch.nn.Conv2d(6, 6, 3, 1, padding=2)

    def forward(self, x):
        v1 = self.conv1(x)
        v2 = torch.tanh(v1)
        v3 = self.conv2(x)
        v4 = torch.tanh(v3)
        return v4




class ModelTanh(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(12, 9, 5, 1, padding=1)

    def forward(self, x):
        v1 = self.conv(x)
        v2 = torch.tanh(v1)
        return v2




func = ModelTanh().to('cuda')



x = torch.randn(2, 1, 3, 3)


test_inputs = [x]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [9, 12, 5, 5], expected input[2, 1, 3, 3] to have 12 channels, but got 1 channels instead

jit:
Failed running call_module L__self___conv(*(FakeTensor(..., device='cuda:0', size=(2, 1, 3, 3)),), **{}):
Given groups=1, weight of size [9, 12, 5, 5], expected input[2, 1, 3, 3] to have 12 channels, but got 1 channels instead

from user code:
   File "<string>", line 39, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''