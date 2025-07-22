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
        self.conv_1 = torch.nn.Conv2d(in_channels=128, out_channels=256, kernel_size=(4, 1), bias=False)
        self.bn = torch.nn.BatchNorm1d(num_features=9216)
        self.tanh = torch.nn.Tanh()

    def forward(self, x0):
        x1 = self.conv_1(x0)
        x1 = torch.tanh(x1)
        x1 = torch.sum(x1, dim=2, keepdim=False)
        x2 = self.bn(x1)
        x3 = torch.tanh(x2)
        return x3




func = ModelTanh().to('cuda')



x0 = torch.randn(1, 128, 64, 1).repeat(1, 1, 1, 64)


test_inputs = [x0]

# JIT_FAIL
'''
direct:
running_mean should contain 256 elements not 9216

jit:
Failed running call_module L__self___bn(*(FakeTensor(..., device='cuda:0', size=(1, 256, 64)),), **{}):
running_mean should contain 256 elements not 9216

from user code:
   File "<string>", line 27, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''