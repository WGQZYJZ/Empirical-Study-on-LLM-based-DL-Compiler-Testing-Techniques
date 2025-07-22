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
        self.conv_transpose = torch.nn.ConvTranspose2d(3, 1, 3, stride=2, padding=1)
        self.conv = torch.nn.Conv2d(1, 1, 3, stride=2, padding=1)

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = self.conv_transpose(v1)
        v3 = v1 * 0.5
        v4 = v2 * 0.5
        v5 = v1 * 0.7071067811865476
        v6 = v2 * 0.7071067811865476
        v7 = torch.erf(v5)
        v8 = torch.erf(v6)
        v9 = v7 + 1
        v10 = v8 + 1
        v11 = v3 * v9
        v12 = v4 * v10
        v13 = v12 + v11
        return v13



func = Model().to('cpu')


x1 = torch.randn(1, 3, 224, 224)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [1, 1, 3, 3], expected input[1, 3, 224, 224] to have 1 channels, but got 3 channels instead

jit:
Failed running call_function <built-in method conv2d of type object at 0x73fdaf996ec0>(*(FakeTensor(..., size=(1, 3, 224, 224)), Parameter(FakeTensor(..., size=(1, 1, 3, 3), requires_grad=True)), Parameter(FakeTensor(..., size=(1,), requires_grad=True)), (2, 2), (1, 1), (1, 1), 1), **{}):
Given groups=1, weight of size [1, 1, 3, 3], expected input[1, 3, 224, 224] to have 1 channels, but got 3 channels instead

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