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
        self.linear = torch.nn.Linear(3, 64)
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1)
        self.relu = torch.nn.ReLU()
        self.linear2 = torch.nn.Linear(8, 8)

    def forward(self, x):
        v1 = self.linear(x)
        v2 = self.conv(x)
        v3 = self.relu(v2)
        v4 = self.linear2(v3)
        return v4


func = Model().to('cpu')


x = torch.rand(1, 3)

test_inputs = [x]

# JIT_FAIL
'''
direct:
Expected 3D (unbatched) or 4D (batched) input to conv2d, but got input of size: [1, 3]

jit:
Failed running call_function <built-in method conv2d of type object at 0x75f239d96ec0>(*(FakeTensor(..., size=(1, 3)), Parameter(FakeTensor(..., size=(8, 3, 1, 1), requires_grad=True)), Parameter(FakeTensor(..., size=(8,), requires_grad=True)), (1, 1), (0, 0), (1, 1), 1), **{}):
Expected 3D (unbatched) or 4D (batched) input to conv2d, but got input of size: [1, 3]

from user code:
   File "<string>", line 24, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 554, in forward
    return self._conv_forward(input, self.weight, self.bias)
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 549, in _conv_forward
    return F.conv2d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''