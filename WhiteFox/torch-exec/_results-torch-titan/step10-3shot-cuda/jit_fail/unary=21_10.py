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
        self.model = torch.nn.Sequential(torch.nn.Conv2d(3, 32, 7, stride=2, padding=2, bias=True, dilation=2), torch.nn.BatchNorm2d(32), torch.nn.MaxPool2d(2), torch.nn.ReLU(), torch.nn.Conv2d(32, 16, 5, stride=2, padding=0, bias=False), torch.nn.Tanh())

    def forward(self, x):
        return self.model(x)




func = ModelTanh().to('cuda')



x = torch.randn(2, 3, 8, 8)


test_inputs = [x]

# JIT_FAIL
'''
direct:
Calculated padded input size per channel: (12 x 12). Kernel size: (13 x 13). Kernel size can't be greater than actual input size

jit:
Failed running call_module L__self___model_0(*(FakeTensor(..., device='cuda:0', size=(2, 3, 8, 8)),), **{}):
Calculated padded input size per channel: (12 x 12). Kernel size: (13 x 13). Kernel size can't be greater than actual input size

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''