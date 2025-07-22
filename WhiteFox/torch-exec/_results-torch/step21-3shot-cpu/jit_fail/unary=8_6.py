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
        self.conv2d = torch.nn.Conv2d(1, 5, (3, 3), stride=(1, 1), padding=(0, 0), dilation=(1, 1), groups=1, bias=True)
        self.conv_transpose = torch.nn.ConvTranspose2d(64, 5, 3, stride=1, padding=1, dilation=1, output_padding=0)

    def forward(self, x1):
        v1 = self.conv2d(x1)
        v1 = self.conv_transpose(v1)
        v2 = v1 + 3
        v3 = torch.clamp(v2, min=0)
        v4 = torch.clamp(v3, max=6)
        v5 = v1 * v4
        v6 = v5 / 6
        return v6



func = Model().to('cpu')


x1 = torch.randn(1, 1, 56, 128)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given transposed=1, weight of size [64, 5, 3, 3], expected input[1, 5, 54, 126] to have 64 channels, but got 5 channels instead

jit:
Failed running call_function <built-in method conv_transpose2d of type object at 0x7c0175596ec0>(*(FakeTensor(..., size=(1, 5, s0 - 2, s1 - 2)), Parameter(FakeTensor(..., size=(64, 5, 3, 3), requires_grad=True)), Parameter(FakeTensor(..., size=(5,), requires_grad=True)), (1, 1), (1, 1), (0, 0), 1, (1, 1)), **{}):
Given transposed=1, weight of size [64, 5, 3, 3], expected input[1, 5, s0 - 2, s1 - 2] to have 64 channels, but got 5 channels instead

from user code:
   File "<string>", line 22, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 1162, in forward
    return F.conv_transpose2d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''