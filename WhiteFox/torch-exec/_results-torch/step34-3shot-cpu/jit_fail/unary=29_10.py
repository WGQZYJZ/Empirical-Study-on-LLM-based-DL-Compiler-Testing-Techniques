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

    def __init__(self, min_value=-0.5, max_value=1):
        super().__init__()
        self.max_pool1d = torch.nn.MaxPool1d(5, stride=2, padding=1, dilation=3)
        self.conv_transpose = torch.nn.ConvTranspose2d(1, 3, 1, stride=2, padding=2)
        self.min_value = min_value
        self.max_value = max_value

    def forward(self, x1):
        v1 = self.conv_transpose(x1)
        v2 = torch.clamp_min(v1, self.min_value)
        v3 = torch.clamp_max(v2, self.max_value)
        v4 = self.max_pool1d(v3)
        return v4



func = Model().to('cpu')


x1 = torch.randn(1, 1, 5, 2)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given input size per channel: (5 x 2). Calculated output size per channel: (5 x -1). Output size is too small

jit:
Failed running call_function <built-in method conv_transpose2d of type object at 0x76d25bb96ec0>(*(FakeTensor(..., size=(1, 1, 5, 2)), Parameter(FakeTensor(..., size=(1, 3, 1, 1), requires_grad=True)), Parameter(FakeTensor(..., size=(3,), requires_grad=True)), (2, 2), (2, 2), (0, 0), 1, (1, 1)), **{}):
Trying to create tensor with negative dimension -1: [1, 3, 5, -1]

from user code:
   File "<string>", line 23, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 1162, in forward
    return F.conv_transpose2d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''