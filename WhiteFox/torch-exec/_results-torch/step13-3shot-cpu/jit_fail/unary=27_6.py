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

    def __init__(self, min_value=1, max_value=-1):
        super().__init__()
        self.fc = torch.nn.Linear(1024, 128)
        self.conv = torch.nn.Conv2d(1, 16, 2, stride=2, padding=1)
        self.min_value = min_value
        self.max_value = max_value

    def forward(self, x1):
        v0 = x1
        v1 = self.fc(v0)
        v2 = self.conv(v1)
        v3 = torch.clamp_min(v2, self.min_value)
        v4 = torch.relu(v2)
        v5 = torch.clamp_max(v4, self.max_value)
        return v5



func = Model().to('cpu')


x1 = torch.randn(2, 1024)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Expected 3D (unbatched) or 4D (batched) input to conv2d, but got input of size: [2, 128]

jit:
Failed running call_function <built-in method conv2d of type object at 0x76b5f8996ec0>(*(FakeTensor(..., size=(2, 128)), Parameter(FakeTensor(..., size=(16, 1, 2, 2), requires_grad=True)), Parameter(FakeTensor(..., size=(16,), requires_grad=True)), (2, 2), (1, 1), (1, 1), 1), **{}):
Expected 3D (unbatched) or 4D (batched) input to conv2d, but got input of size: [2, 128]

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