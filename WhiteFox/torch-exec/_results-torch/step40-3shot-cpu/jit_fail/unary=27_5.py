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

    def __init__(self, min, max):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 3, (1,), stride=(1,), padding=(0,))
        self.min = min
        self.max = max

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.clamp_min(v1, self.min)
        v3 = torch.clamp_max(v2, self.max)
        return v3


min = 1692758127
max = 1724832688

func = Model(min, max).to('cpu')


x1 = torch.randn(1, 3, 800, 800)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
expected dilation to be a single integer value or a list of 1 values to match the convolution dimensions, but got dilation=[1, 1]

jit:
Failed running call_function <built-in method conv2d of type object at 0x7cec39b96ec0>(*(FakeTensor(..., size=(1, 3, s1, s2)), Parameter(FakeTensor(..., size=(3, 3, 1), requires_grad=True)), Parameter(FakeTensor(..., size=(3,), requires_grad=True)), (1,), (0,), (1, 1), 1), **{}):
tuple index out of range

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