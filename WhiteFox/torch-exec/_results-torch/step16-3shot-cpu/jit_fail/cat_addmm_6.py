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

class Model(nn.Module):

    def __init__(self):
        super().__init__()
        self.conv = nn.Conv2d(1, 1, 1, bias=False)

    def forward(self, x):
        x = self.conv(x)
        x = torch.cat((x, x), dim=1)
        return x



func = Model().to('cpu')


x = torch.randn(2, 2, 2, 2)

test_inputs = [x]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [1, 1, 1, 1], expected input[2, 2, 2, 2] to have 1 channels, but got 2 channels instead

jit:
Failed running call_function <built-in method conv2d of type object at 0x7f0d65396ec0>(*(FakeTensor(..., size=(s0, s1, s2, s3)), Parameter(FakeTensor(..., size=(1, 1, 1, 1), requires_grad=True)), None, (1, 1), (0, 0), (1, 1), 1), **{}):
Given groups=1, weight of size [1, 1, 1, 1], expected input[s0, s1, s2, s3] to have 1 channels, but got s1 channels instead

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