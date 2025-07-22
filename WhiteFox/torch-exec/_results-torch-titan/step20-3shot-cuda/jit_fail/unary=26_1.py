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

    def __init__(self, negative_slope):
        super().__init__()
        self.negative_slope = negative_slope
        self.conv_t1 = torch.nn.ConvTranspose2d(144, 96, 1, stride=1, dilation=2, padding=2)
        self.conv_t2 = torch.nn.ConvTranspose2d(96, 96, 3, stride=2, dilation=1, padding=1)
        self.conv_t3 = torch.nn.ConvTranspose2d(96, 144, 3, stride=2, dilation=1, padding=1)
        self.conv_t4 = torch.nn.ConvTranspose2d(144, 72, 2, stride=1, dilation=1, padding=1)
        self.conv_t5 = torch.nn.ConvTranspose2d(72, 28, 3, stride=1, dilation=1, padding=1)
        self.conv_t6 = torch.nn.ConvTranspose2d(28, 3, 3, stride=1, dilation=1, padding=1)

    def forward(self, x1):
        x2 = self.conv_t1(x1)
        x3 = self.conv_t2(x2)
        x4 = self.conv_t3(x3)
        x5 = self.conv_t4(x4)
        x6 = self.conv_t5(x5)
        x7 = self.conv_t6(x6)
        x8 = ((x7 + x1) + self.negative_slope)
        x9 = (x8 > 0)
        x10 = (x8 - self.negative_slope)
        x11 = torch.where(x9, x8, x10)
        return x11




negative_slope = (- 0.02)


func = Model(negative_slope).to('cuda')

x1 = 1

test_inputs = [x1]

# JIT_FAIL
'''
direct:
conv_transpose2d(): argument 'input' (position 1) must be Tensor, not int

jit:
Failed running call_module L__self___conv_t1(*(1,), **{}):
conv_transpose2d(): argument 'input' (position 1) must be Tensor, not int

from user code:
   File "<string>", line 28, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''