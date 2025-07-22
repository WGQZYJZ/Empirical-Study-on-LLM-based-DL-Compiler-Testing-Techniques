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
        self.conv1 = torch.nn.Conv2d(3, 16, 3, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(16, 16, 3, stride=1, padding=1, groups=2)

    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = torch.relu(v1)
        v3 = torch.transpose(v2, 1, 0)
        v4 = torch.transpose(v2, 1, 3)
        v32 = self.conv2(v3)
        v42 = self.conv2(v4)
        v33 = torch.transpose(v32, 0, 2)
        v43 = torch.transpose(v42, 0, 2)
        v5 = torch.cat([v33, v43], 0)
        v6 = torch.relu(v5)
        return v6



func = Model().to('cpu')


x1 = torch.randn(1, 3, 224, 224)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given groups=2, weight of size [16, 8, 3, 3], expected input[16, 1, 224, 224] to have 16 channels, but got 1 channels instead

jit:
Failed running call_function <built-in method conv2d of type object at 0x7f97a2996ec0>(*(FakeTensor(..., size=(16, 1, s0, s1)), Parameter(FakeTensor(..., size=(16, 8, 3, 3), requires_grad=True)), Parameter(FakeTensor(..., size=(16,), requires_grad=True)), (1, 1), (1, 1), (1, 1), 2), **{}):
Given groups=2, weight of size [16, 8, 3, 3], expected input[16, 1, s0, s1] to have 16 channels, but got 1 channels instead

from user code:
   File "<string>", line 25, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 554, in forward
    return self._conv_forward(input, self.weight, self.bias)
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 549, in _conv_forward
    return F.conv2d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''