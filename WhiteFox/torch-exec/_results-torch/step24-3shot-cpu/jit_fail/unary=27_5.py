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

    def __init__(self, min_value=0.123, max_value=0.1234):
        super().__init__()
        self.conv = torch.nn.Conv2d(16, 16, 1, stride=-2, padding=123)
        self.min_value = min_value
        self.max_value = max_value

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.clamp_min(v1, self.min_value)
        v3 = torch.clamp_max(v2, self.max_value)
        return v3



func = Model().to('cpu')


x1 = torch.randn(1, 16, 64, 64)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
non-positive stride is not supported

jit:
Failed running call_function <built-in method conv2d of type object at 0x7caff2196ec0>(*(FakeTensor(..., size=(1, 16, 64, 64)), Parameter(FakeTensor(..., size=(16, 16, 1, 1), requires_grad=True)), Parameter(FakeTensor(..., size=(16,), requires_grad=True)), (-2, -2), (123, 123), (1, 1), 1), **{}):
non-positive stride is not supported

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