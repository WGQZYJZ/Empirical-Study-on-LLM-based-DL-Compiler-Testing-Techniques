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
        self.conv_transpose = torch.nn.ConvTranspose2d(4, 24, kernel_size=(1, 5), stride=(1, 5), padding=6)
        self.conv_transpose1 = torch.nn.ConvTranspose2d(24, 29, kernel_size=(3, 5), stride=(3, 5), padding=6)
        self.conv_transpose2 = torch.nn.ConvTranspose2d(29, 42, kernel_size=(4, 5), stride=(4, 5), padding=6)

    def forward(self, x1):
        v1 = self.conv_transpose(x1)
        v2 = v1 * 0.5
        v3 = v1 * v1 * v1
        v4 = v3 * 0.044715
        v5 = v1 + v4
        v6 = v5 * 0.7978845608028654
        v7 = torch.tanh(v6)
        v8 = v7 + 1
        v9 = v2 * v8
        return v9



func = Model().to('cpu')


x1 = torch.randn(1, 4, 8, 232)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given input size per channel: (8 x 232). Calculated output size per channel: (-4 x 1148). Output size is too small

jit:
Failed running call_function <built-in method conv_transpose2d of type object at 0x78d766f96ec0>(*(FakeTensor(..., size=(1, 4, 8, 232)), Parameter(FakeTensor(..., size=(4, 24, 1, 5), requires_grad=True)), Parameter(FakeTensor(..., size=(24,), requires_grad=True)), (1, 5), (6, 6), (0, 0), 1, (1, 1)), **{}):
Trying to create tensor with negative dimension -4: [1, 24, -4, 1148]

from user code:
   File "<string>", line 22, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 1162, in forward
    return F.conv_transpose2d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''