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
        self.conv1 = torch.nn.Conv2d(3, 128, kernel_size=(1, 1), stride=(1, 1), bias=False)
        self.conv2 = torch.nn.ConvTranspose2d(in_channels=128, out_channels=64, kernel_size=(1, 1), stride=(1, 1), bias=False)
        self.conv3 = torch.nn.Conv2d(64, 1, 1)

    def forward(self, x):
        out = self.conv2(x)
        out = self.conv3(out)
        return out




func = Model().to('cuda')



x1 = torch.randn(1, 3, 256, 64)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given transposed=1, weight of size [128, 64, 1, 1], expected input[1, 3, 256, 64] to have 128 channels, but got 3 channels instead

jit:
Failed running call_module L__self___conv2(*(FakeTensor(..., device='cuda:0', size=(1, 3, 256, 64)),), **{}):
Given transposed=1, weight of size [128, 64, 1, 1], expected input[1, 3, 256, 64] to have 128 channels, but got 3 channels instead

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''