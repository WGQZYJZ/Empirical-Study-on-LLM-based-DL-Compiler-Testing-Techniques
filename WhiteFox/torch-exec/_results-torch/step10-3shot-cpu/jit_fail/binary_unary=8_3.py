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

class Model2(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x1):
        v1 = self.conv(x1)
        v3 = torch.nn.functional.interpolate(v1, scale_factor=0.5, recompute_scale_factor=True)
        v4 = torch.relu(v3)
        return v4



func = Model2().to('cpu')


x1 = torch.randint(255, (1, 3, 64, 64))

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Input type (long int) and bias type (float) should be the same

jit:
Failed running call_function <built-in method conv2d of type object at 0x7f881f796ec0>(*(FakeTensor(..., size=(1, 3, 64, 64), dtype=torch.int64), Parameter(FakeTensor(..., size=(8, 3, 1, 1), requires_grad=True)), Parameter(FakeTensor(..., size=(8,), requires_grad=True)), (1, 1), (1, 1), (1, 1), 1), **{}):
Input type (long int) and bias type (float) should be the same

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