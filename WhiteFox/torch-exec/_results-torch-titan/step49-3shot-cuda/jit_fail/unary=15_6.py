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
        self.layer_1 = torch.nn.Sequential(torch.nn.Conv3d(3, 64, kernel_size=(3, 3, 3), stride=(1, 1, 1), bias=True), torch.nn.ReLU())
        self.layer_2 = torch.nn.Sequential(torch.nn.Conv3d(1, 1, kernel_size=(1, 1, 1), stride=(1, 1, 1), bias=False), torch.nn.ReLU())

    def forward(self, z):
        v1 = self.layer_1(z)
        v2 = self.layer_2(v1)
        return v2




func = Model().to('cuda')



x = torch.randn(1, 3, 49, 512, 437)


test_inputs = [x]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [1, 1, 1, 1, 1], expected input[1, 64, 47, 510, 435] to have 1 channels, but got 64 channels instead

jit:
Failed running call_module L__self___layer_2_0(*(FakeTensor(..., device='cuda:0', size=(1, 64, 47, 510, 435)),), **{}):
Given groups=1, weight of size [1, 1, 1, 1, 1], expected input[1, 64, 47, 510, 435] to have 1 channels, but got 64 channels instead

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''