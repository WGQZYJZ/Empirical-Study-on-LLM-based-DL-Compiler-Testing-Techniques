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
        self.conv2d = torch.nn.ConvTranspose2d(2, 2, 3, bias=True)
        self.conv2d_1 = torch.nn.ConvTranspose2d(5, 2, kernel_size=(5, 3), bias=False)
        self.conv2d_2 = torch.nn.ConvTranspose2d(4, 5, kernel_size=(2, 4), stride=(1, 2), bias=None)

    def forward(self, x1):
        v1 = self.conv2d(x1)
        v2 = v1.detach()
        v3 = self.conv2d_1(v2)
        v4 = self.conv2d_2(v1)
        v5 = v4.detach()
        return v5




func = Model().to('cuda')



x1 = torch.randn(7, 4, 20, 10)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given transposed=1, weight of size [2, 2, 3, 3], expected input[7, 4, 20, 10] to have 2 channels, but got 4 channels instead

jit:
Failed running call_module L__self___conv2d(*(FakeTensor(..., device='cuda:0', size=(7, 4, 20, 10)),), **{}):
Given transposed=1, weight of size [2, 2, 3, 3], expected input[7, 4, 20, 10] to have 2 channels, but got 4 channels instead

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''