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
        self.conv = torch.nn.Conv3d(32, 32, 3, padding=(2, 1, 0), stride=(2, 2, 2), bias=False)

    def forward(self, x1):
        x2 = F.relu(x1)
        x3 = F.avg_pool3d(x2, (3, 3, 3), stride=1, padding=1, count_include_pad=True)
        x3 = F.relu(x3)
        x4 = self.conv(x3)
        x5 = F.relu(x4)
        x6 = F.avg_pool3d(x5, (1, 3, 3), stride=1, padding=(1, 1, 1), count_include_pad=False)
        x7 = F.sigmoid(x6)
        return x7



func = Model().to('cpu')


x1 = torch.randn(1, 32, 22, 22, 12)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
pad should be at most half of effective kernel size, but got pad=1, kernel_size=1 and dilation=1

jit:
Failed running call_function <built-in function avg_pool3d>(*(FakeTensor(..., size=(1, 32, 12, 11, 5)), (1, 3, 3)), **{'stride': 1, 'padding': (1, 1, 1), 'count_include_pad': False}):
pad should be at most half of effective kernel size, but got pad=1, kernel_size=1 and dilation=1

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''