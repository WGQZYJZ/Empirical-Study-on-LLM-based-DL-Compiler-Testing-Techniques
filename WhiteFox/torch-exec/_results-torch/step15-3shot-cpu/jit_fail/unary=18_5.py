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
        self.conv1 = torch.nn.Conv2d(in_channels=16, out_channels=2, kernel_size=11, stride=11, padding=11)
        self.conv2 = torch.nn.Conv2d(in_channels=2, out_channels=12, kernel_size=1, stride=3, padding=1)
        self.conv3 = torch.nn.Conv2d(in_channels=12, out_channels=24, kernel_size=3, stride=1, padding=1)

    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = torch.sigmoid(v1)
        v2 = v2.view(1, 2400)
        v3 = self.conv2(v2)
        v4 = torch.sigmoid(v3)
        v4 = v4.view(1, 720)
        v5 = self.conv3(v4)
        v6 = torch.sigmoid(v5)
        v6 = v6.view(1, 120)
        return v6



func = Model().to('cpu')


x1 = torch.randn(1, 16, 64, 64)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
shape '[1, 2400]' is invalid for input of size 98

jit:
Failed running call_method view(*(FakeTensor(..., size=(1, 2, 7, 7)), 1, 2400), **{}):
shape '[1, 2400]' is invalid for input of size 98

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''