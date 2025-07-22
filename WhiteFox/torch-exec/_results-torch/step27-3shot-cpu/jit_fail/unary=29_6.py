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

    def __init__(self, min_value=-0.3, max_value=-0.1):
        super().__init__()
        self.tanh = torch.nn.Tanh()
        self.conv_transpose = torch.nn.ConvTranspose2d(3, 8, 1, stride=1, padding=1)
        self.act_4 = torch.nn.Tanh()
        self.min_value = min_value
        self.max_value = max_value

    def forward(self, x2):
        v1 = self.conv_transpose(x2)
        v2 = torch.clamp_min(v1, self.min_value)
        v3 = torch.clamp_max(v2, self.max_value)
        v4 = self.tanh(v3)
        v9 = self.act_4(v4)
        return v9



func = Model().to('cpu')


x2 = torch.randn(1, 3, 1, 5)

test_inputs = [x2]

# JIT_FAIL
'''
direct:
Given input size per channel: (1 x 5). Calculated output size per channel: (-1 x 3). Output size is too small

jit:
Failed running call_function <built-in method conv_transpose2d of type object at 0x7234c3f96ec0>(*(FakeTensor(..., size=(1, 3, 1, 5)), Parameter(FakeTensor(..., size=(3, 8, 1, 1), requires_grad=True)), Parameter(FakeTensor(..., size=(8,), requires_grad=True)), (1, 1), (1, 1), (0, 0), 1, (1, 1)), **{}):
Trying to create tensor with negative dimension -1: [1, 8, -1, 3]

from user code:
   File "<string>", line 24, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 1162, in forward
    return F.conv_transpose2d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''