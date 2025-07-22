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
        self.conv = torch.nn.Conv2d(32, 32, 1, stride=2, padding=6)

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.clamp_min(v1, min=0.0)
        v3 = torch.clamp_max(v2, max=1.0)
        return v3



func = Model().to('cpu')


x1 = torch.randn(1, 32, 100, 10, 100)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Expected 3D (unbatched) or 4D (batched) input to conv2d, but got input of size: [1, 32, 100, 10, 100]

jit:
Failed running call_function <built-in method conv2d of type object at 0x7f7a91b96ec0>(*(FakeTensor(..., size=(1, 32, 100, 10, 100)), Parameter(FakeTensor(..., size=(32, 32, 1, 1), requires_grad=True)), Parameter(FakeTensor(..., size=(32,), requires_grad=True)), (2, 2), (6, 6), (1, 1), 1), **{}):
Expected 3D (unbatched) or 4D (batched) input to conv2d, but got input of size: [1, 32, 100, 10, 100]

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