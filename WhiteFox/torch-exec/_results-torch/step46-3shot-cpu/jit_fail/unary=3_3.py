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
        self.conv = torch.nn.Conv2d(33, 3, (3, 3), stride=(1, 1), padding=(1, 1))
        self.conv2 = torch.nn.Conv2d(32, 3, (1, 1), stride=(1, 1), padding=(0, 0))
        self.conv3 = torch.nn.Conv2d(26, 3, (1, 1), stride=(1, 1), padding=(0, 0))

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 * 0.5
        v3 = v1 * 0.7071067811865476
        v4 = torch.erf(v3)
        v5 = v4 + 1
        v6 = v2 * v5
        v7 = self.conv2(x1)
        v8 = v7 * 0.5
        v9 = v7 * 0.7071067811865476
        v10 = torch.erf(v9)
        v11 = v10 + 1
        v12 = v8 * v11
        v13 = self.conv3(v12)
        return v13



func = Model().to('cpu')


x1 = torch.randn(1, 16, 79, 78)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [3, 33, 3, 3], expected input[1, 16, 79, 78] to have 33 channels, but got 16 channels instead

jit:
Failed running call_function <built-in method conv2d of type object at 0x7e84cc196ec0>(*(FakeTensor(..., size=(1, s0, s1, s2)), Parameter(FakeTensor(..., size=(3, 33, 3, 3), requires_grad=True)), Parameter(FakeTensor(..., size=(3,), requires_grad=True)), (1, 1), (1, 1), (1, 1), 1), **{}):
Given groups=1, weight of size [3, 33, 3, 3], expected input[1, s0, s1, s2] to have 33 channels, but got s0 channels instead

from user code:
   File "<string>", line 22, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 554, in forward
    return self._conv_forward(input, self.weight, self.bias)
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 549, in _conv_forward
    return F.conv2d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''