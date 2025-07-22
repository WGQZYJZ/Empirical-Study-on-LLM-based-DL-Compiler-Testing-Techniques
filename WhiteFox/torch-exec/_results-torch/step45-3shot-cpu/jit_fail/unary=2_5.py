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
        self.conv2d = torch.nn.Conv2d(8, 26, 9)
        self.conv_transpose = torch.nn.ConvTranspose2d(26, 9, 2, stride=2, padding=3, dilation=2, output_padding=2)

    def forward(self, x1):
        v1 = self.conv2d(x1)
        v2 = torch.flatten(v1, start_dim=1)
        v3 = torch.reshape(v2, (x1.shape[0], 26, 5, 5))
        v4 = self.conv_transpose(v3) * 0.7978845608028654
        v5 = torch.flatten(v4, start_dim=1)
        v6 = torch.reshape(v5, (x1.shape[0], 18, 2, 4))
        return v6



func = Model().to('cpu')


x1 = torch.randn(32, 8, 2, 4)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Calculated padded input size per channel: (2 x 4). Kernel size: (9 x 9). Kernel size can't be greater than actual input size

jit:
Failed running call_function <built-in method conv2d of type object at 0x728f67b96ec0>(*(FakeTensor(..., size=(32, 8, 2, 4)), Parameter(FakeTensor(..., size=(26, 8, 9, 9), requires_grad=True)), Parameter(FakeTensor(..., size=(26,), requires_grad=True)), (1, 1), (0, 0), (1, 1), 1), **{}):
Calculated padded input size per channel: (2 x 4). Kernel size: (9 x 9). Kernel size can't be greater than actual input size

from user code:
   File "<string>", line 21, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 554, in forward
    return self._conv_forward(input, self.weight, self.bias)
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 549, in _conv_forward
    return F.conv2d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''