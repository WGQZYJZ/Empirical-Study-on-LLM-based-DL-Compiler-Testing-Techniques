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

    def __init__(self, min_value=1.98, max_value=1.58):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose2d(1, 1, 1, stride=2, dilation=2, groups=1, bias=True, padding=3, output_padding=0)
        self.min_value = min_value
        self.max_value = max_value

    def forward(self, x1):
        v1 = self.conv_transpose(x1)
        v2 = torch.clamp_min(v1, self.min_value)
        v3 = torch.clamp_max(v2, self.max_value)
        return v3



func = Model().to('cpu')


x1 = torch.randn(1, 1, 2, 3)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given input size per channel: (2 x 3). Calculated output size per channel: (-3 x -1). Output size is too small

jit:
Failed running call_function <built-in method conv_transpose2d of type object at 0x708655796ec0>(*(FakeTensor(..., size=(1, 1, s0, s1)), Parameter(FakeTensor(..., size=(1, 1, 1, 1), requires_grad=True)), Parameter(FakeTensor(..., size=(1,), requires_grad=True)), (2, 2), (3, 3), (0, 0), 1, (2, 2)), **{}):
Trying to create tensor with negative dimension 2*s0 - 7: [1, 1, 2*s0 - 7, 2*s1 - 7]

from user code:
   File "<string>", line 22, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 1162, in forward
    return F.conv_transpose2d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''