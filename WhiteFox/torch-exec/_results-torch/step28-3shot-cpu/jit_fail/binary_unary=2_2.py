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
        self.conv1 = torch.nn.Conv2d(3, 32, 3, stride=2, padding=1)
        self.conv2 = torch.nn.Conv2d(32, 32, 3, stride=2, padding=1)
        self.conv3 = torch.nn.Conv2d(32, 32, 3, stride=2, padding=1)
        self.conv4 = torch.nn.Conv2d(32, 32, 3, stride=2, padding=1)
        self.conv5 = torch.nn.Conv2d(32, 32, 3, stride=2, padding=1)
        self.conv6 = torch.nn.Conv2d(32, 32, 3, stride=2, padding=1)
        self.conv7 = torch.nn.Conv2d(32, 32, 3, stride=2, padding=1)
        self.conv8 = torch.nn.Conv2d(32, 32, 3, stride=2, padding=1)
        self.conv9 = torch.nn.Conv2d(32, 32, 3, stride=2, padding=1)

    def forward(self, x1, x2, x3):
        v1 = self.conv1(x1) + self.conv9(x3)
        v2 = v1 - 2
        v3 = F.relu(v2)
        v4 = self.conv2(v3) + self.conv8(x2)
        v5 = v4 - 0.3
        v6 = F.relu(v5)
        v7 = self.conv3(v6) + self.conv7(x1)
        v8 = v7 - 0.7
        v9 = F.relu(v8)
        v10 = self.conv4(v9) + self.conv6(x3)
        v11 = v10 - 1.2
        v12 = F.relu(v11)
        v13 = self.conv5(v12) + self.conv9(x2)
        v14 = v13 - 1.8
        v15 = F.relu(v14)
        v16 = v15 + 1.5
        return v16



func = Model().to('cpu')


x2 = torch.randn(1, 3, 64, 64)

x3 = torch.randn(1, 3, 128, 128)

x1 = torch.randn(1, 3, 128, 128)

test_inputs = [x2, x3, x1]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [32, 32, 3, 3], expected input[1, 3, 128, 128] to have 32 channels, but got 3 channels instead

jit:
Failed running call_function <built-in method conv2d of type object at 0x7003caf96ec0>(*(FakeTensor(..., size=(1, 3, 128, 128)), Parameter(FakeTensor(..., size=(32, 32, 3, 3), requires_grad=True)), Parameter(FakeTensor(..., size=(32,), requires_grad=True)), (2, 2), (1, 1), (1, 1), 1), **{}):
Given groups=1, weight of size [32, 32, 3, 3], expected input[1, 3, 128, 128] to have 32 channels, but got 3 channels instead

from user code:
   File "<string>", line 28, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 554, in forward
    return self._conv_forward(input, self.weight, self.bias)
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 549, in _conv_forward
    return F.conv2d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''