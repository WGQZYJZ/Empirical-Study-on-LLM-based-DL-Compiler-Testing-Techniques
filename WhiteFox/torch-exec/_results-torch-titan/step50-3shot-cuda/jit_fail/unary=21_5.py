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
        self.sigmoid = torch.nn.Sigmoid()
        self.tanh = torch.nn.Tanh()
        self.conv = torch.nn.Conv2d(1, 3, 1, bias=True)
        self.conv2 = torch.nn.Conv2d(1, 8, 3, stride=2, padding=1)
        self.conv3 = torch.nn.Conv2d(8, 12, 2, stride=2, padding=1)

    def forward(self, x):
        v1 = self.conv(x)
        v2 = self.tanh(v1)
        v3 = self.conv2(v2)
        v4 = self.tanh(v3)
        v5 = self.conv3(v4)
        v6 = self.tanh(v5)
        return v6




func = ModelTanh().to('cuda')



x = torch.rand(2, 1, 28, 28)


test_inputs = [x]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [8, 1, 3, 3], expected input[2, 3, 28, 28] to have 1 channels, but got 3 channels instead

jit:
Failed running call_module L__self___conv2(*(FakeTensor(..., device='cuda:0', size=(2, 3, 28, 28)),), **{}):
Given groups=1, weight of size [8, 1, 3, 3], expected input[2, 3, 28, 28] to have 1 channels, but got 3 channels instead

from user code:
   File "<string>", line 28, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''