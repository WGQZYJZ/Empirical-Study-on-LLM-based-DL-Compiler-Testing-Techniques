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
        self.relu6 = torch.nn.ReLU6()
        self.conv2d = torch.nn.Conv2d(64, 256, 1, 1)
        self.conv2d_1 = torch.nn.Conv2d(64, 128, 1, 1)
        self.conv2d_2 = torch.nn.Conv2d(128, 128, 3, 2, 1)
        self.conv2d_3 = torch.nn.Conv2d(128, 256, 1, 1)

    def forward(self, x):
        v1 = self.relu6(x)
        v2 = self.conv2d(v1)
        v3 = self.relu6(v2)
        v4 = self.conv2d_1(v3)
        v5 = self.relu6(v4)
        v6 = (v5,)
        v7 = self.conv2d_2(*v6)
        v8 = self.relu6(v7)
        v9 = self.conv2d_3(v8)
        v10 = self.relu6(v9)
        v11 = v10 + v10
        v12 = self.conv2d_1(v11)
        v13 = self.relu6(v12)
        return v13



func = Model().to('cpu')


x = torch.randn(1, 64, 224, 224)

test_inputs = [x]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [128, 64, 1, 1], expected input[1, 256, 224, 224] to have 64 channels, but got 256 channels instead

jit:
Failed running call_function <built-in method conv2d of type object at 0x77e58df96ec0>(*(FakeTensor(..., size=(1, 256, 224, 224)), Parameter(FakeTensor(..., size=(128, 64, 1, 1), requires_grad=True)), Parameter(FakeTensor(..., size=(128,), requires_grad=True)), (1, 1), (0, 0), (1, 1), 1), **{}):
Given groups=1, weight of size [128, 64, 1, 1], expected input[1, 256, 224, 224] to have 64 channels, but got 256 channels instead

from user code:
   File "<string>", line 27, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 554, in forward
    return self._conv_forward(input, self.weight, self.bias)
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 549, in _conv_forward
    return F.conv2d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''