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
        self.conv_t1 = torch.nn.ConvTranspose2d(3, 5, 1, stride=2, padding=0, output_padding=1)
        self.conv_t2 = torch.nn.ConvTranspose2d(2, 1, 1, stride=1, padding=0, output_padding=0)
        self.conv_t3 = torch.nn.ConvTranspose2d(1, 7, 3, stride=1, padding=1)

    def forward(self, x1):
        v1 = self.conv_t1(x1)
        v2 = self.conv_t2(v1)
        v3 = self.conv_t3(v2)
        v4 = v3 * 0.5
        v5 = v3 * v3 * v3
        v6 = v5 * 0.044715
        v7 = v3 + v6
        v8 = v7 * 0.7978845608028654
        v9 = torch.tanh(v8)
        v10 = v9 + 1
        v11 = v4 * v10
        return v11



func = Model().to('cpu')


x1 = torch.randn(2, 3, 6, 6)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given transposed=1, weight of size [2, 1, 1, 1], expected input[2, 5, 12, 12] to have 2 channels, but got 5 channels instead

jit:
Failed running call_function <built-in method conv_transpose2d of type object at 0x7eb217796ec0>(*(FakeTensor(..., size=(2, 5, 12, 12)), Parameter(FakeTensor(..., size=(2, 1, 1, 1), requires_grad=True)), Parameter(FakeTensor(..., size=(1,), requires_grad=True)), (1, 1), (0, 0), (0, 0), 1, (1, 1)), **{}):
Given transposed=1, weight of size [2, 1, 1, 1], expected input[2, 5, 12, 12] to have 2 channels, but got 5 channels instead

from user code:
   File "<string>", line 23, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 1162, in forward
    return F.conv_transpose2d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''