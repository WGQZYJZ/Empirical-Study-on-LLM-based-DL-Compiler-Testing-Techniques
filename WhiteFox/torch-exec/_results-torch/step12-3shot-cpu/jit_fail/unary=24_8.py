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
        self.conv1 = torch.nn.Conv3d(8, 32, 4, stride=1, padding=3)
        self.conv2 = torch.nn.Conv2d(32, 32, 2, stride=1, padding=1)

    def forward(self, x):
        negative_slope = 1
        v1 = self.conv1(x)
        v2 = self.conv2(v1)
        v3 = v2 > 0
        v4 = v2 * negative_slope
        v5 = torch.where(v3, v2, v4)
        return v5



func = Model().to('cpu')


x1 = torch.randn(4, 8, 56, 56, 56)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Expected 3D (unbatched) or 4D (batched) input to conv2d, but got input of size: [4, 32, 59, 59, 59]

jit:
Failed running call_function <built-in method conv2d of type object at 0x7aec85596ec0>(*(FakeTensor(..., size=(4, 32, 59, 59, 59)), Parameter(FakeTensor(..., size=(32, 32, 2, 2), requires_grad=True)), Parameter(FakeTensor(..., size=(32,), requires_grad=True)), (1, 1), (1, 1), (1, 1), 1), **{}):
Expected 3D (unbatched) or 4D (batched) input to conv2d, but got input of size: [4, 32, 59, 59, 59]

from user code:
   File "<string>", line 23, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 554, in forward
    return self._conv_forward(input, self.weight, self.bias)
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 549, in _conv_forward
    return F.conv2d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''