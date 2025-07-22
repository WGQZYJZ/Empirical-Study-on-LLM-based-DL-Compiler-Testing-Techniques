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
        self.conv_transpose = torch.nn.ConvTranspose2d(3, 4, 3, bias=False)
        self.relu = torch.nn.ReLU()
        self.conv = torch.nn.Conv2d(12, 3, 1)

    def forward(self, x1):
        v1 = self.conv_transpose(x1)
        v2 = self.relu(v1)
        v3 = v1 * 0.5
        v4 = v1 * v1 * v1
        v5 = v4 * 0.044715
        v6 = v1 + v5
        v7 = v6 * 0.7978845608028654
        v8 = torch.tanh(v7)
        v9 = v8 + 1
        v10 = v3 * v9
        v11 = torch.cat((v2, v10), 1)
        v12 = self.conv(v11)
        return v12



func = Model().to('cpu')


x1 = torch.randn(2, 3, 5, 5)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [3, 12, 1, 1], expected input[2, 8, 7, 7] to have 12 channels, but got 8 channels instead

jit:
Failed running call_function <built-in method conv2d of type object at 0x78137d196ec0>(*(FakeTensor(..., size=(s0, 8, s2 + 2, s3 + 2)), Parameter(FakeTensor(..., size=(3, 12, 1, 1), requires_grad=True)), Parameter(FakeTensor(..., size=(3,), requires_grad=True)), (1, 1), (0, 0), (1, 1), 1), **{}):
Given groups=1, weight of size [3, 12, 1, 1], expected input[s0, 8, s2 + 2, s3 + 2] to have 12 channels, but got 8 channels instead

from user code:
   File "<string>", line 33, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 554, in forward
    return self._conv_forward(input, self.weight, self.bias)
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 549, in _conv_forward
    return F.conv2d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''