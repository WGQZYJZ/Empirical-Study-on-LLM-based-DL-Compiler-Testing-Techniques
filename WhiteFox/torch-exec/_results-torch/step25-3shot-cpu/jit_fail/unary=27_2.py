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

    def __init__(self, min):
        super().__init__()
        self.conv = torch.nn.Conv1d(3, 8, kernel_size=1)
        self.relu = torch.nn.ReLU()
        self.min = min

    def forward(self, input, min, max):
        v1 = self.conv(input)
        v2 = self.relu(v1)
        v3 = torch.clamp_min(v2, min)
        v4 = torch.clamp_max(v3, max)
        return v4


min = 50

func = Model(min).to('cpu')


input = torch.randn(1, 3, 64, 64)
min = 1
max = 1

test_inputs = [input, min, max]

# JIT_FAIL
'''
direct:
Expected 2D (unbatched) or 3D (batched) input to conv1d, but got input of size: [1, 3, 64, 64]

jit:
Failed running call_function <built-in method conv1d of type object at 0x753b33b96ec0>(*(FakeTensor(..., size=(1, 3, 64, 64)), Parameter(FakeTensor(..., size=(8, 3, 1), requires_grad=True)), Parameter(FakeTensor(..., size=(8,), requires_grad=True)), (1,), (0,), (1,), 1), **{}):
Expected 2D (unbatched) or 3D (batched) input to conv1d, but got input of size: [1, 3, 64, 64]

from user code:
   File "<string>", line 22, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 375, in forward
    return self._conv_forward(input, self.weight, self.bias)
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 370, in _conv_forward
    return F.conv1d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''