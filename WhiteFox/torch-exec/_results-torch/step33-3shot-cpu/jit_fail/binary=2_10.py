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
        self.conv1 = torch.nn.Conv2d(128, 64, 1, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(64, 64, 2, stride=1, padding=1)
        self.conv3 = torch.nn.Conv3d(64, 2, 3, stride=1, padding=1)

    def forward(self, x):
        v1 = self.conv1(x)
        v2 = self.conv2(v1)
        v3 = self.conv3(v2)
        v4 = v3 - 5
        return v4



func = Model().to('cpu')


x = torch.randn(1, 128, 8, 8, 8)

test_inputs = [x]

# JIT_FAIL
'''
direct:
Expected 3D (unbatched) or 4D (batched) input to conv2d, but got input of size: [1, 128, 8, 8, 8]

jit:
Failed running call_function <built-in method conv2d of type object at 0x76208f596ec0>(*(FakeTensor(..., size=(1, 128, 8, 8, 8)), Parameter(FakeTensor(..., size=(64, 128, 1, 1), requires_grad=True)), Parameter(FakeTensor(..., size=(64,), requires_grad=True)), (1, 1), (1, 1), (1, 1), 1), **{}):
Expected 3D (unbatched) or 4D (batched) input to conv2d, but got input of size: [1, 128, 8, 8, 8]

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