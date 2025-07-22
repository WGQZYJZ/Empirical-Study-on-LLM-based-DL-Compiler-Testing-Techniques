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
        self.conv_transpose_1 = torch.nn.ConvTranspose2d(128, 85, 3, stride=2, padding=1)
        self.conv_transpose_2 = torch.nn.ConvTranspose2d(75, 60, 5, stride=1, padding=2)
        self.conv_transpose_3 = torch.nn.ConvTranspose2d(39, 56, 5, stride=1, padding=2)
        self.conv_transpose_4 = torch.nn.ConvTranspose2d(61, 54, 5, stride=1, padding=2)
        self.conv_transpose_5 = torch.nn.ConvTranspose2d(65, 54, 5, stride=1, padding=2)
        self.conv_transpose_6 = torch.nn.ConvTranspose2d(63, 32, 5, stride=2, padding=1)
        self.conv_transpose_7 = torch.nn.ConvTranspose2d(40, 1, 1, stride=2, padding=1)

    def forward(self, x1):
        v1 = self.conv_transpose_1(x1)
        v2 = torch.sigmoid(v1)
        v3 = v1 * v2
        v4 = self.conv_transpose_2(v3)
        v5 = torch.sigmoid(v4)
        v6 = v4 * v5
        v7 = self.conv_transpose_3(v6)
        v8 = torch.sigmoid(v7)
        v9 = v7 * v8
        v10 = self.conv_transpose_4(v9)
        v11 = torch.sigmoid(v10)
        v12 = v10 * v11
        v13 = self.conv_transpose_5(v12)
        v14 = torch.sigmoid(v13)
        v15 = v13 * v14
        v16 = self.conv_transpose_6(v15)
        v17 = torch.sigmoid(v16)
        v18 = v16 * v17
        v19 = self.conv_transpose_7(v18)
        return v19



func = Model().to('cpu')


x1 = torch.randn(2, 128, 56, 56)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given transposed=1, weight of size [75, 60, 5, 5], expected input[2, 85, 111, 111] to have 75 channels, but got 85 channels instead

jit:
Failed running call_function <built-in method conv_transpose2d of type object at 0x7b1ab5d96ec0>(*(FakeTensor(..., size=(2, 85, 111, 111)), Parameter(FakeTensor(..., size=(75, 60, 5, 5), requires_grad=True)), Parameter(FakeTensor(..., size=(60,), requires_grad=True)), (1, 1), (2, 2), (0, 0), 1, (1, 1)), **{}):
Given transposed=1, weight of size [75, 60, 5, 5], expected input[2, 85, 111, 111] to have 75 channels, but got 85 channels instead

from user code:
   File "<string>", line 29, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 1162, in forward
    return F.conv_transpose2d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''