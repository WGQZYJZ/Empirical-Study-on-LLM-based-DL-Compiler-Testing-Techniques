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
        self.conv = torch.nn.Conv2d(12, 20, 4, stride=3, padding=1)
        self.conv_transpose = torch.nn.ConvTranspose2d(20, 32, 3, stride=2)
        self.conv_transpose_2 = torch.nn.ConvTranspose2d(32, 32, 4, stride=2, padding=1)
        self.conv_transpose_3 = torch.nn.ConvTranspose2d(32, 32, 2, stride=2, padding=1)
        self.conv_transpose_4 = torch.nn.ConvTranspose2d(32, 3, 2, stride=1, padding=0)

    def forward(self, x0):
        v0 = self.conv(x0)
        v1 = self.conv_transpose(v0)
        v2 = self.conv_transpose_2(v1)
        v4 = self.conv_transpose_4(v2)
        v3 = self.conv_transpose_3(v4)
        v5 = v3 + 3
        v6 = torch.clamp_min(v5, 0)
        v7 = torch.clamp_max(v6, 6)
        v8 = v7 / 6
        return v8



func = Model().to('cpu')


x0 = torch.randn(1, 12, 64, 64)

test_inputs = [x0]

# JIT_FAIL
'''
direct:
Given transposed=1, weight of size [32, 32, 2, 2], expected input[1, 3, 87, 87] to have 32 channels, but got 3 channels instead

jit:
Failed running call_function <built-in method conv_transpose2d of type object at 0x7a0cf3596ec0>(*(FakeTensor(..., size=(1, 3, 87, 87)), Parameter(FakeTensor(..., size=(32, 32, 2, 2), requires_grad=True)), Parameter(FakeTensor(..., size=(32,), requires_grad=True)), (2, 2), (1, 1), (0, 0), 1, (1, 1)), **{}):
Given transposed=1, weight of size [32, 32, 2, 2], expected input[1, 3, 87, 87] to have 32 channels, but got 3 channels instead

from user code:
   File "<string>", line 28, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 1162, in forward
    return F.conv_transpose2d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''