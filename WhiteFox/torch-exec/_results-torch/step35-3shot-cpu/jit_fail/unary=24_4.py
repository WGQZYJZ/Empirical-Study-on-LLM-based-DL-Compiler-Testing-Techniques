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
        self.conv0 = torch.nn.Conv2d(32, 8, 3, stride=2, padding=1)
        self.conv1 = torch.nn.Conv2d(8, 8, 1)
        self.conv_transpose = torch.nn.ConvTranspose2d(3, 1, kernel_size=(4, 4), stride=(2, 2), padding=(1, 1), groups=1, bias=False)

    def forward(self, x):
        negative_slope = 0.5
        v1 = self.conv0(x)
        v2 = self.conv1(v1)
        v3 = torch.relu(v2)
        v4 = torch.relu(v3)
        v5 = self.conv_transpose(v4)
        v6 = v5 > 0
        v7 = v5 * negative_slope
        v8 = torch.where(v6, v5, v7)
        return v8



func = Model().to('cpu')


x1 = torch.randn(1, 32, 128, 128)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given transposed=1, weight of size [3, 1, 4, 4], expected input[1, 8, 64, 64] to have 3 channels, but got 8 channels instead

jit:
Failed running call_function <built-in method conv_transpose2d of type object at 0x7e1b8e396ec0>(*(FakeTensor(..., size=(1, 8, 64, 64)), Parameter(FakeTensor(..., size=(3, 1, 4, 4), requires_grad=True)), None, (2, 2), (1, 1), (0, 0), 1, (1, 1)), **{}):
Given transposed=1, weight of size [3, 1, 4, 4], expected input[1, 8, 64, 64] to have 3 channels, but got 8 channels instead

from user code:
   File "<string>", line 27, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 1162, in forward
    return F.conv_transpose2d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''