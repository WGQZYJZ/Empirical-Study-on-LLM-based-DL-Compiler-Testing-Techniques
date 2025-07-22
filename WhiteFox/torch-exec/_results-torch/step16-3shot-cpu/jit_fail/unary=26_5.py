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
        self.conv_t = torch.nn.ConvTranspose2d(256, 256, 5, stride=2, padding=1)
        self.conv_t1 = torch.nn.ConvTranspose2d(256, 256, 4, stride=3, padding=0)
        self.conv_t3 = torch.nn.ConvTranspose2d(256, 256, 7, stride=2, padding=1)
        self.conv_c5 = torch.nn.Conv2d(256, 256, 5, stride=1, padding=2)
        self.conv_t7 = torch.nn.ConvTranspose2d(256, 128, 2, stride=1, padding=0)
        self.conv_t8 = torch.nn.ConvTranspose2d(128, 64, 3, stride=1, padding=0)
        self.conv_t10 = torch.nn.ConvTranspose2d(64, 2, 2, stride=2, padding=0)

    def forward(self, x9):
        (x1, x2, x3, x4, x5, x6, x7) = x9.split([64, 160, 160, 16, 320, 64, 128], 1)
        x8 = x7 > 0
        x9 = x7 * -0.15
        x10 = torch.where(x8, x7, x9)
        return torch.cat([x1, x2, x3, x4, x5, x6, x10], 1)



func = Model().to('cpu')


x9 = torch.randn(8, 512, 4, 4)

test_inputs = [x9]

# JIT_FAIL
'''
direct:
split_with_sizes expects split_sizes to sum exactly to 512 (input tensor's size at dimension 1), but got split_sizes=[64, 160, 160, 16, 320, 64, 128]

jit:
Failed running call_method split(*(FakeTensor(..., size=(8, 512, 4, 4)), [64, 160, 160, 16, 320, 64, 128], 1), **{}):
Split sizes add up to 912 but got the tensor's size of 512

from user code:
   File "<string>", line 26, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''