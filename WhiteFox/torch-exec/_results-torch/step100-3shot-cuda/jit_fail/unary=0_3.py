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
        self.conv = torch.nn.Conv2d(5, 12, 10, stride=5, dilation=2, padding=3)

    def forward(self, x104):
        v1 = self.conv(x104)
        v2 = v1 * 0.5
        v3 = v1 * v1
        v4 = v3 * v1
        v5 = v4 * 0.044715
        v6 = v1 + v5
        v7 = v6 * 0.7978845608028654
        v8 = torch.tanh(v7)
        v9 = v8 + 1
        v10 = v2 * v9
        return v10



func = Model().to('cuda')


x104 = torch.randn(1, 5, 12, 48)

test_inputs = [x104]

# JIT_FAIL
'''
direct:
Calculated padded input size per channel: (18 x 54). Kernel size: (19 x 19). Kernel size can't be greater than actual input size

jit:
Failed running call_function <built-in method conv2d of type object at 0x78414bf96ec0>(*(FakeTensor(..., device='cuda:0', size=(1, 5, 12, 48)), Parameter(FakeTensor(..., device='cuda:0', size=(12, 5, 10, 10), requires_grad=True)), Parameter(FakeTensor(..., device='cuda:0', size=(12,), requires_grad=True)), (5, 5), (3, 3), (2, 2), 1), **{}):
Calculated padded input size per channel: (18 x 54). Kernel size: (19 x 19). Kernel size can't be greater than actual input size

from user code:
   File "<string>", line 20, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 554, in forward
    return self._conv_forward(input, self.weight, self.bias)
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 549, in _conv_forward
    return F.conv2d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''