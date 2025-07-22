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



class Model(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.conv_bn_relu = torch.nn.Sequential(torch.nn.Conv2d(12, 16, 5), torch.nn.BatchNorm2d(16), torch.nn.ReLU(inplace=True))
        self.conv_relu = torch.nn.Sequential(torch.nn.Conv2d(6, 16, 5), torch.nn.ReLU(inplace=True))

    def forward(self, x):
        x = self.conv_bn_relu(x)
        x = self.conv_relu(x)
        return x




func = Model().to('cuda')



x = torch.randn(2, 12, 5, 5)


test_inputs = [x]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [16, 6, 5, 5], expected input[2, 16, 1, 1] to have 6 channels, but got 16 channels instead

jit:
Failed running call_module L__self___conv_relu_0(*(FakeTensor(..., device='cuda:0', size=(2, 16, 1, 1)),), **{}):
Given groups=1, weight of size [16, 6, 5, 5], expected input[2, 16, 1, 1] to have 6 channels, but got 16 channels instead

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''