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
        super(ModelTanh, self).__init__()
        self.conv_1 = torch.nn.Conv2d(128, 128, 3)
        self.conv_2 = torch.nn.Conv2d(128, 1, 1)
        self.conv_3 = torch.nn.Conv2d(128, 128, 3)
        self.conv_4 = torch.nn.Conv2d(128, 128, 3, padding=1)
        self.conv_5 = torch.nn.Conv2d(128, 128, 3)

    def forward(self, x1):
        x2 = self.conv_1(x1)
        x2 = torch.tanh(x2)
        x3 = self.conv_2(x2)
        x4 = self.conv_3(x3)
        x5 = self.conv_4(x4)
        x6 = self.conv_5(x4)
        x4 = torch.tanh((x5 + x6))
        x4 = (x4 + x1)
        return x4




func = ModelTanh().to('cuda')



x1 = torch.randn(1, 128, 16, 16)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [128, 128, 3, 3], expected input[1, 1, 14, 14] to have 128 channels, but got 1 channels instead

jit:
Failed running call_module L__self___conv_3(*(FakeTensor(..., device='cuda:0', size=(1, 1, 14, 14)),), **{}):
Given groups=1, weight of size [128, 128, 3, 3], expected input[1, 1, 14, 14] to have 128 channels, but got 1 channels instead

from user code:
   File "<string>", line 29, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''