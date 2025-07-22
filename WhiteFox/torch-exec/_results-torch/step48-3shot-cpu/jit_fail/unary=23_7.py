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
        self.conv_transpose = torch.nn.ConvTranspose2d(1, 1, 3)
        self.pooling = torch.nn.MaxPool1d(1)

    def forward(self, x1):
        v1 = self.conv_transpose(x1)
        v2 = self.pooling(v1)
        v3 = F.adaptive_avg_pool2d(v2, (1, 2))
        return v3



func = Model().to('cpu')


x1 = torch.randn(1, 1, 3, 3)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
max_pool1d: Expected 2D or 3D (batch mode) tensor with optional 0 dim batch size for input, but got:[1, 1, 5, 5]

jit:
Failed running call_function <function boolean_dispatch.<locals>.fn at 0x7d4f6e0a1d30>(*(FakeTensor(..., size=(1, 1, s0 + 2, s1 + 2)), 1, 1, 0, 1), **{'ceil_mode': False, 'return_indices': False}):
max_pool1d: Expected 2D or 3D (batch mode) tensor with optional 0 dim batch size for input, but got:[1, 1, s0 + 2, s1 + 2]

from user code:
   File "<string>", line 22, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/pooling.py", line 134, in forward
    return F.max_pool1d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''