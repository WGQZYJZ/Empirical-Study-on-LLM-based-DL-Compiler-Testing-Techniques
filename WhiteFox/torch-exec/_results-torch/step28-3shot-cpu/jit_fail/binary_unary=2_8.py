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

    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = v1 - 2
        v3 = F.relu(v2)
        v4 = self.conv1(x1)
        v5 = v1 + 1.3
        v6 = F.relu(v5)
        v7 = v3 - 0.2
        v8 = F.relu(v7)
        v9 = torch.cat([v6, v8], 1)
        v10 = self.conv2(v9)
        v11 = v10 - 0.5
        v12 = F.relu(v11)
        v13 = self.conv2(v9)
        v14 = v10 - 1.6
        v15 = F.relu(v14)
        v16 = self.conv3(v15)
        v17 = v16 - 3.4
        v18 = F.relu(v17)
        v19 = self.conv2(v9)
        v20 = v10 - 0.3
        v21 = F.relu(v20)
        v22 = torch.add(v19, v21)
        v23 = F.relu(v22)
        v24 = torch.floor_divide(v23, 100)
        v25 = v24 + 14
        v26 = v25.size()
        return v26



func = Model().to('cpu')


x1 = torch.randn(1, 3, 3, 3)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [32, 32, 3, 3], expected input[1, 64, 2, 2] to have 32 channels, but got 64 channels instead

jit:
Failed running call_function <built-in method conv2d of type object at 0x7003caf96ec0>(*(FakeTensor(..., size=(1, 64, 2, 2)), Parameter(FakeTensor(..., size=(32, 32, 3, 3), requires_grad=True)), Parameter(FakeTensor(..., size=(32,), requires_grad=True)), (2, 2), (1, 1), (1, 1), 1), **{}):
Given groups=1, weight of size [32, 32, 3, 3], expected input[1, 64, 2, 2] to have 32 channels, but got 64 channels instead

from user code:
   File "<string>", line 33, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 554, in forward
    return self._conv_forward(input, self.weight, self.bias)
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 549, in _conv_forward
    return F.conv2d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''