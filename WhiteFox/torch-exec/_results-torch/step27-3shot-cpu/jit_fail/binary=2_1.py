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
        self.conv = torch.nn.Conv2d(3, 5, 1, stride=1, padding=1)
        self.conv1 = torch.nn.Conv2d(3, 5, 1, stride=1, padding=1)

    def forward(self, x):
        v1 = self.conv(x)
        v2 = self.conv1(torch.tensor([[0.1, 0.1, 0.1], [-0.1, -0.1, -0.1], [-0.1, -0.1, -0.1]]))
        return v1 + v2



func = Model().to('cpu')


x = torch.randn(1, 3, 64, 64)

test_inputs = [x]

# JIT_FAIL
'''
direct:
Expected 3D (unbatched) or 4D (batched) input to conv2d, but got input of size: [3, 3]

jit:
Failed running call_function <built-in method conv2d of type object at 0x7ed8d1f96ec0>(*(FakeTensor(..., size=(3, 3)), Parameter(FakeTensor(..., size=(5, 3, 1, 1), requires_grad=True)), Parameter(FakeTensor(..., size=(5,), requires_grad=True)), (1, 1), (1, 1), (1, 1), 1), **{}):
Expected 3D (unbatched) or 4D (batched) input to conv2d, but got input of size: [3, 3]

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