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
        self.conv_transpose = torch.nn.ConvTranspose2d(3, 8, 3, stride=1, padding=1)
        self.conv_transpose_1 = torch.nn.ConvTranspose2d(8, 8, 3, stride=1, padding=1)

    def forward(self, x1):
        v1 = self.conv_transpose(x1)
        v2 = self.conv_transpose_1(v1)
        v3 = torch.sigmoid(v2)
        v4 = v2 * v3
        v5 = self.conv_transpose(v4)
        v6 = self.conv_transpose_1(v3)
        v7 = torch.sigmoid(v4)
        v8 = v4 * v7
        v9 = v5 + v8
        return v9



func = Model().to('cpu')


x1 = torch.randn(1, 3, 16, 16)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given transposed=1, weight of size [3, 8, 3, 3], expected input[1, 8, 16, 16] to have 3 channels, but got 8 channels instead

jit:
Failed running call_function <built-in method conv_transpose2d of type object at 0x780c7a396ec0>(*(FakeTensor(..., size=(1, 8, s1, s2)), Parameter(FakeTensor(..., size=(3, 8, 3, 3), requires_grad=True)), Parameter(FakeTensor(..., size=(8,), requires_grad=True)), (1, 1), (1, 1), (0, 0), 1, (1, 1)), **{}):
Given transposed=1, weight of size [3, 8, 3, 3], expected input[1, 8, s1, s2] to have 3 channels, but got 8 channels instead

from user code:
   File "<string>", line 25, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 1162, in forward
    return F.conv_transpose2d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''