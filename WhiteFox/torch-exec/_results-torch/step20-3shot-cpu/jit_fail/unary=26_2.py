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

    def __init__(self, stride, padding, dilation):
        super().__init__()
        self.conv_t = torch.nn.ConvTranspose2d(int(480 * 7 / 8 + 0.5), 7, 2, stride=stride, padding=padding, dilation=dilation)

    def forward(self, x1):
        x2 = self.conv_t(x1)
        x3 = x2
        x4 = x3 > 0
        x5 = x3 * 0.5
        x6 = torch.where(x4, x3, x5)
        return x6


stride = 2
padding = 1
dilation = 1

func = Model(stride, padding, dilation).to('cpu')


x1 = torch.randn(32, 480, 16, 16)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given transposed=1, weight of size [420, 7, 2, 2], expected input[32, 480, 16, 16] to have 420 channels, but got 480 channels instead

jit:
Failed running call_function <built-in method conv_transpose2d of type object at 0x7f8d88f96ec0>(*(FakeTensor(..., size=(s0, s1, s2, s3)), Parameter(FakeTensor(..., size=(420, 7, 2, 2), requires_grad=True)), Parameter(FakeTensor(..., size=(7,), requires_grad=True)), (2, 2), (1, 1), (0, 0), 1, (1, 1)), **{}):
Given transposed=1, weight of size [420, 7, 2, 2], expected input[s0, s1, s2, s3] to have 420 channels, but got s1 channels instead

from user code:
   File "<string>", line 20, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 1162, in forward
    return F.conv_transpose2d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''