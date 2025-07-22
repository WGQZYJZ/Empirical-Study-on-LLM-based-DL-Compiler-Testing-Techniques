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
        self.conv = torch.nn.Conv2d(2, 16, kernel_size=(3, 3), stride=2, padding=1, dilation=1)
        self.conv_transpose = torch.nn.ConvTranspose2d(15, 16, 14, stride=2, padding=1, output_padding=3)

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = self.conv_transpose(v1)
        v3 = v2 * 0.5
        v4 = v2 * v2 * v2
        v5 = v4 * 0.044715
        v6 = v2 + v5
        v7 = v6 * 0.7978845608028654
        v8 = torch.tanh(v7)
        v9 = v8 + 1
        v10 = v3 * v8
        return v10



func = Model().to('cpu')


x1 = torch.randn(3, 2, 16, 16)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given transposed=1, weight of size [15, 16, 14, 14], expected input[3, 16, 8, 8] to have 15 channels, but got 16 channels instead

jit:
Failed running call_function <built-in method conv_transpose2d of type object at 0x7d3dd0796ec0>(*(FakeTensor(..., size=(s0, 16, (((s2 - 1)//2)) + 1, (((s3 - 1)//2)) + 1)), Parameter(FakeTensor(..., size=(15, 16, 14, 14), requires_grad=True)), Parameter(FakeTensor(..., size=(16,), requires_grad=True)), (2, 2), (1, 1), (3, 3), 1, (1, 1)), **{}):
Given transposed=1, weight of size [15, 16, 14, 14], expected input[s0, 16, (((s2 - 1)//2)) + 1, (((s3 - 1)//2)) + 1] to have 15 channels, but got 16 channels instead

from user code:
   File "<string>", line 22, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 1162, in forward
    return F.conv_transpose2d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''