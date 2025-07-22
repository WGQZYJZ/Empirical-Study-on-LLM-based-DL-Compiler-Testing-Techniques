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
        self.conv_transpose2d = torch.nn.ConvTranspose2d(3, 8, 3, stride=3, padding=1)
        self.maxpool = torch.nn.MaxPool2d(3, stride=2, padding=1)
        self.conv_transpose = torch.nn.ConvTranspose2d(32, 8, 3, stride=2, padding=1)

    def forward(self, x1):
        v1 = self.conv_transpose2d(x1)
        v2 = self.maxpool(v1)
        v3 = self.conv_transpose(v2)
        v4 = v3 * 0.49999999999999994
        v5 = v3 * 0.5000000000000001
        v6 = torch.erf(v5)
        v7 = v6 + 1
        v8 = v4 * v7
        return v8



func = Model().to('cpu')


x1 = torch.randn(1, 3, 30, 30)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given transposed=1, weight of size [32, 8, 3, 3], expected input[1, 8, 44, 44] to have 32 channels, but got 8 channels instead

jit:
Failed running call_function <built-in method conv_transpose2d of type object at 0x7a785d996ec0>(*(FakeTensor(..., size=(1, 8, 44, 44)), Parameter(FakeTensor(..., size=(32, 8, 3, 3), requires_grad=True)), Parameter(FakeTensor(..., size=(8,), requires_grad=True)), (2, 2), (1, 1), (0, 0), 1, (1, 1)), **{}):
Given transposed=1, weight of size [32, 8, 3, 3], expected input[1, 8, 44, 44] to have 32 channels, but got 8 channels instead

from user code:
   File "<string>", line 24, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 1162, in forward
    return F.conv_transpose2d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''