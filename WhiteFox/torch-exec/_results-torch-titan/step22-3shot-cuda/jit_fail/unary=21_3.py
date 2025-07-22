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



class f(torch.nn.Module):

    def forward(self, x1):
        x2 = torch.nn.functional.softplus(x1)
        x3 = torch.nn.functional.tanh(x1)
        x4 = torch.nn.functional.tanh(x2)
        result = torch.add(x1, x3, x4, x3)
        return result




class ModelTanh(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.conv_1 = torch.nn.Conv2d(3, 6, 3, stride=2, padding=1)
        self.conv_2 = torch.nn.Conv2d(6, 9, 3, stride=2, padding=1)
        self.conv_3 = torch.nn.Conv2d(9, 12, 3, stride=1, padding=1)
        self.conv_4 = torch.nn.Conv2d(9, 15, 3, stride=1, padding=1)
        self.f = f()

    def forward(self, x):
        v1 = self.conv_1(x)
        v2 = self.conv_2(v1)
        v3 = self.conv_3(v2)
        v4 = self.conv_4(v1)
        v5 = self.f(v3)
        v6 = self.f(v4)
        result = torch.add(v1, v5, v2, v6)
        return result




func = ModelTanh().to('cuda')



x = torch.randn(1, 3, 256, 256)


test_inputs = [x]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [15, 9, 3, 3], expected input[1, 6, 128, 128] to have 9 channels, but got 6 channels instead

jit:
Failed running call_module L__self___conv_4(*(FakeTensor(..., device='cuda:0', size=(1, 6, 128, 128)),), **{}):
Given groups=1, weight of size [15, 9, 3, 3], expected input[1, 6, 128, 128] to have 9 channels, but got 6 channels instead

from user code:
   File "<string>", line 41, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''