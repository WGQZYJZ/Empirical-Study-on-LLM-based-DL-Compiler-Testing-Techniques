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
        self.conv_transpose = torch.nn.ConvTranspose2d(3, 2, 5, padding=[1, 2, 1, 0], stride=3, dilation=2, groups=1, bias=False)

    def forward(self, x1):
        v1 = self.conv_transpose(x1)
        v2 = v1 + 3
        v3 = torch.clamp_min(v2, 0)
        v4 = torch.clamp_max(v3, 6)
        v5 = v4 / 6
        return v5



func = Model().to('cpu')


x1 = torch.randn(1, 3, 64, 64)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
expected padding to be a single integer value or a list of 2 values to match the convolution dimensions, but got padding=[1, 2, 1, 0]

jit:
Failed running call_function <built-in method conv_transpose2d of type object at 0x7b528f596ec0>(*(FakeTensor(..., size=(1, s0, s1, s2)), Parameter(FakeTensor(..., size=(3, 2, 5, 5), requires_grad=True)), None, (3, 3), (1, 2, 1, 0), (0, 0), 1, (2, 2)), **{}):
expected padding to be a single integer value or a list of 2 values to match the convolution dimensions, but got padding=[1, 2, 1, 0]

from user code:
   File "<string>", line 20, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 1162, in forward
    return F.conv_transpose2d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''