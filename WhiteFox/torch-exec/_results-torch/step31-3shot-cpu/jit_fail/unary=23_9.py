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
        self.conv_transpose1 = torch.nn.ConvTranspose2d(3, 16, kernel_size=3, stride=1, padding=1, dilation=1, groups=1, bias=False)
        self.avg1 = torch.nn.AvgPool2d(kernel_size=3, stride=1, padding=1, ceil_mode=True, count_include_pad=True)
        self.conv_transpose2 = torch.nn.ConvTranspose2d(16, 24, kernel_size=3, stride=1, padding=1, dilation=1, groups=1, bias=False)
        self.batch2 = torch.nn.BatchNorm2d(24)
        self.fc = torch.nn.Linear(1408, 3)

    def forward(self, x1):
        v0 = self.conv_transpose1(x1)
        v4 = self.avg1(v0)
        v1 = self.conv_transpose2(v4)
        v5 = self.batch2(v1)
        v2 = v5.reshape(1, 1408)
        v3 = self.fc(v2)
        v6 = torch.tanh(v3)
        return v6



func = Model().to('cpu')


x1 = torch.randn(1, 3, 256, 256)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
shape '[1, 1408]' is invalid for input of size 1572864

jit:
Failed running call_method reshape(*(FakeTensor(..., size=(1, 24, 256, 256)), 1, 1408), **{}):
shape '[1, 1408]' is invalid for input of size 1572864

from user code:
   File "<string>", line 28, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''