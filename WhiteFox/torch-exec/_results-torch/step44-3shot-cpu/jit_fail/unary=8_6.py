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
        self.conv_transpose = torch.nn.ConvTranspose1d(64, 31, 10, stride=-2, padding=-3, output_padding=-3)

    def forward(self, x1):
        v1 = self.conv_transpose(x1)
        v2 = v1 + 3
        v3 = torch.clamp(v2, min=0)
        v4 = torch.clamp(v3, max=6)
        v5 = v1 * v4
        v6 = v5 / 6
        return v6



func = Model().to('cpu')


x1 = torch.randn(1, 64, 61)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
negative padding is not supported

jit:
Failed running call_function <built-in method conv_transpose1d of type object at 0x78a6dc996ec0>(*(FakeTensor(..., size=(1, s0, s1)), Parameter(FakeTensor(..., size=(64, 31, 10), requires_grad=True)), Parameter(FakeTensor(..., size=(31,), requires_grad=True)), (-2,), (-3,), (-3,), 1, (1,)), **{}):
Trying to create tensor with negative dimension 15 - 2*s1: [1, 31, 15 - 2*s1]

from user code:
   File "<string>", line 20, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 974, in forward
    return F.conv_transpose1d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''