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
        self.conv1 = torch.nn.Conv3d(1, 2, kernel_size=[16, 3, 99], stride=[4, 1, 2])
        self.conv2 = torch.nn.Conv2d(2, 4, kernel_size=3, stride=2)

    def forward(self, x2):
        v3 = self.conv1(x2)
        v4 = self.conv2(v3)
        v5 = v4 * 0.5
        v7 = v5 * 0.707106
        v6 = v5 * float('1e-22')
        v8 = v6 * 0.507106
        v9 = v8 * 0.707106
        v10 = v9 * 0.707106
        return v10



func = Model().to('cpu')


x2 = torch.randn(1, 1, 24, 487, 799)

test_inputs = [x2]

# JIT_FAIL
'''
direct:
Expected 3D (unbatched) or 4D (batched) input to conv2d, but got input of size: [1, 2, 3, 485, 351]

jit:
Failed running call_function <built-in method conv2d of type object at 0x7c7dc1d96ec0>(*(FakeTensor(..., size=(1, 2, ((s0//4)) - 3, 485, (((s2 - 99)//2)) + 1)), Parameter(FakeTensor(..., size=(4, 2, 3, 3), requires_grad=True)), Parameter(FakeTensor(..., size=(4,), requires_grad=True)), (2, 2), (0, 0), (1, 1), 1), **{}):
Expected 3D (unbatched) or 4D (batched) input to conv2d, but got input of size: [1, 2, 3, 485, 351]

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