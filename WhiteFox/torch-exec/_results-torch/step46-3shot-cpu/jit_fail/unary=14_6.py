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
        self.maxpool2d_1 = torch.nn.MaxPool2d(3, stride=3, padding=3)
        self.maxpool2d_2 = torch.nn.MaxPool2d(3, stride=1, padding=0, dilation=1, ceil_mode=False)
        self.conv_transpose = torch.nn.ConvTranspose2d(3, 3, 3, stride=1, padding=0, output_padding=0, groups=1, dilation=1)

    def forward(self, x1, x2):
        v1 = self.maxpool2d_1(x1)
        v2 = self.maxpool2d_2(x2)
        v3 = torch.max(v1, v2)
        v4 = torch.sigmoid(v3)
        v5 = self.conv_transpose(v4)
        v6 = v5 * v3
        return v6



func = Model().to('cpu')


x1 = torch.randn(1, 3, 256, 256)

x2 = torch.randn(1, 3, 256, 256)

test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
pad should be at most half of effective kernel size, but got pad=3, kernel_size=3 and dilation=1

jit:
Failed running call_function <function boolean_dispatch.<locals>.fn at 0x705ddef61ee0>(*(FakeTensor(..., size=(1, 3, 256, 256)), 3, 3, 3, 1), **{'ceil_mode': False, 'return_indices': False}):
pad should be at most half of effective kernel size, but got pad=3, kernel_size=3 and dilation=1

from user code:
   File "<string>", line 22, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/pooling.py", line 213, in forward
    return F.max_pool2d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''