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
        self.conv = torch.nn.Conv2d(3, 4, 2)
        self.bn = torch.nn.BatchNorm2d(1)

    def forward(self, x):
        x = torch.flatten(x, 1)
        x = self.conv(x)
        x = torch.flatten(x, 1)
        x = self.bn(x)
        return x



func = Model().to('cpu')


x = torch.randn(1, 3, 16, 16)

test_inputs = [x]

# JIT_FAIL
'''
direct:
Expected 3D (unbatched) or 4D (batched) input to conv2d, but got input of size: [1, 768]

jit:
Failed running call_function <built-in method conv2d of type object at 0x799ff0796ec0>(*(FakeTensor(..., size=(1, s0*s1*s2)), Parameter(FakeTensor(..., size=(4, 3, 2, 2), requires_grad=True)), Parameter(FakeTensor(..., size=(4,), requires_grad=True)), (1, 1), (0, 0), (1, 1), 1), **{}):
Expected 3D (unbatched) or 4D (batched) input to conv2d, but got input of size: [1, 768]

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