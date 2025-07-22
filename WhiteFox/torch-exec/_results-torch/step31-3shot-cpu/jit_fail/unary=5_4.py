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
        self.conv_transpose_1 = torch.nn.ConvTranspose2d(4, 64, 8, stride=8, padding=4)
        self.conv_transpose_2 = torch.nn.ConvTranspose2d(1, 32, 8, stride=1, padding=8)

    def forward(self, x1):
        t1 = self.conv_transpose_2(self.conv_transpose_1(x1))
        v1 = t1 * 0.5
        v2 = t1 * 0.7071067811865476
        v3 = torch.erf(v2)
        v4 = v3 + 1
        v5 = v1 * v4
        return v5



func = Model().to('cpu')


x1 = torch.randn(1, 1, 255, 80)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given transposed=1, weight of size [4, 64, 8, 8], expected input[1, 1, 255, 80] to have 4 channels, but got 1 channels instead

jit:
Failed running call_function <built-in method conv_transpose2d of type object at 0x7d85a7d96ec0>(*(FakeTensor(..., size=(1, 1, 255, 80)), Parameter(FakeTensor(..., size=(4, 64, 8, 8), requires_grad=True)), Parameter(FakeTensor(..., size=(64,), requires_grad=True)), (8, 8), (4, 4), (0, 0), 1, (1, 1)), **{}):
Given transposed=1, weight of size [4, 64, 8, 8], expected input[1, 1, 255, 80] to have 4 channels, but got 1 channels instead

from user code:
   File "<string>", line 21, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 1162, in forward
    return F.conv_transpose2d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''