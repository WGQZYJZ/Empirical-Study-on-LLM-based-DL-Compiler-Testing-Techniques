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
        self.conv1 = torch.nn.Conv2d(3, 3, 3, stride=2, padding=1)
        self.conv2 = torch.nn.Conv2d(3, 3, 3, stride=2, padding=1)

    def forward(self, x):
        v1 = self.conv1(x)
        v2 = v1.max(1, True)[0]
        v3 = v2 > 0
        v4 = v2 * -0.1
        v5 = torch.where(v3, v2, v4)
        return self.conv2(v5)



func = Model().to('cpu')


x1 = torch.randn(1, 3, 16, 16)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [3, 3, 3, 3], expected input[1, 1, 8, 8] to have 3 channels, but got 1 channels instead

jit:
Failed running call_function <built-in method conv2d of type object at 0x7ff350796ec0>(*(FakeTensor(..., size=(1, 1, (((s0 - 1)//2)) + 1, (((s1 - 1)//2)) + 1)), Parameter(FakeTensor(..., size=(3, 3, 3, 3), requires_grad=True)), Parameter(FakeTensor(..., size=(3,), requires_grad=True)), (2, 2), (1, 1), (1, 1), 1), **{}):
Given groups=1, weight of size [3, 3, 3, 3], expected input[1, 1, (((s0 - 1)//2)) + 1, (((s1 - 1)//2)) + 1] to have 3 channels, but got 1 channels instead

from user code:
   File "<string>", line 26, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 554, in forward
    return self._conv_forward(input, self.weight, self.bias)
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 549, in _conv_forward
    return F.conv2d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''