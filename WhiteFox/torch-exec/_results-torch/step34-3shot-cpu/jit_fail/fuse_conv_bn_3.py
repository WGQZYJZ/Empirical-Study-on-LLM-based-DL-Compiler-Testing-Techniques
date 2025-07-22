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
        self.conv1 = torch.nn.Conv1d(7, 7, 3)
        self.batchnorm3d = torch.nn.BatchNorm3d(7)

    def forward(self, x1):
        s = self.conv1(x1)
        y = self.batchnorm3d(s)
        return y



func = Model().to('cpu')


x1 = torch.rand(1, 7, 11, 11)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Expected 2D (unbatched) or 3D (batched) input to conv1d, but got input of size: [1, 7, 11, 11]

jit:
Failed running call_function <built-in method conv1d of type object at 0x70248a796ec0>(*(FakeTensor(..., size=(1, 7, 11, 11)), Parameter(FakeTensor(..., size=(7, 7, 3), requires_grad=True)), Parameter(FakeTensor(..., size=(7,), requires_grad=True)), (1,), (0,), (1,), 1), **{}):
Expected 2D (unbatched) or 3D (batched) input to conv1d, but got input of size: [1, 7, 11, 11]

from user code:
   File "<string>", line 21, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 375, in forward
    return self._conv_forward(input, self.weight, self.bias)
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 370, in _conv_forward
    return F.conv1d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''