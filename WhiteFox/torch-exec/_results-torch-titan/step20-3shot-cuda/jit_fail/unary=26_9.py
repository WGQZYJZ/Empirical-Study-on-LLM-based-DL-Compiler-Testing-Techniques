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
        self.conv_t = torch.nn.ConvTranspose2d(672, 232, 1, stride=1)
        self.conv_t_1 = torch.nn.ConvTranspose2d(672, 232, 1, stride=1)
        self.conv_t_2 = torch.nn.ConvTranspose2d(768, 768, 1, stride=2)
        self.conv_t_3 = torch.nn.ConvTranspose2d(768, 768, 1, stride=1)

    def forward(self, x1, x2):
        x3 = self.conv_t(x1)
        x4 = self.conv_t_1(x2)
        x5 = torch.cat([x3, x4], dim=1)
        x6 = self.conv_t_2(x5)
        x7 = (x6 <= 0)
        x8 = (x6 * 0.5)
        x9 = torch.where(x7, x6, x8)
        x10 = self.conv_t_3(x9)
        return x10




func = Model().to('cuda')



x1 = torch.randn(32, 672, 56, 56)



x2 = torch.randn(32, 768, 28, 28)


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
Given transposed=1, weight of size [672, 232, 1, 1], expected input[32, 768, 28, 28] to have 672 channels, but got 768 channels instead

jit:
Failed running call_module L__self___conv_t_1(*(FakeTensor(..., device='cuda:0', size=(32, 768, 28, 28)),), **{}):
Given transposed=1, weight of size [672, 232, 1, 1], expected input[32, 768, 28, 28] to have 672 channels, but got 768 channels instead

from user code:
   File "<string>", line 26, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''