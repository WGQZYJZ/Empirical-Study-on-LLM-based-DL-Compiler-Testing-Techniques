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
        torch.manual_seed(1)
        self.conv1 = torch.nn.Conv1d(1, 1, 3)
        torch.manual_seed(1)
        self.bn = torch.nn.BatchNorm1d(1)

    def forward(self, x):
        x1 = self.conv1(x)
        y1 = self.bn(x1)
        x1 = self.conv1(x1)
        y1 = self.bn(x1)
        return y1



func = Model().to('cpu')


x = torch.randn(1, 1, 4, 4)

test_inputs = [x]

# JIT_FAIL
'''
direct:
Expected 2D (unbatched) or 3D (batched) input to conv1d, but got input of size: [1, 1, 4, 4]

jit:
Failed running call_function <built-in method conv1d of type object at 0x723d65996ec0>(*(FakeTensor(..., size=(1, 1, 4, 4)), Parameter(FakeTensor(..., size=(1, 1, 3), requires_grad=True)), Parameter(FakeTensor(..., size=(1,), requires_grad=True)), (1,), (0,), (1,), 1), **{}):
Expected 2D (unbatched) or 3D (batched) input to conv1d, but got input of size: [1, 1, 4, 4]

from user code:
   File "<string>", line 23, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 375, in forward
    return self._conv_forward(input, self.weight, self.bias)
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 370, in _conv_forward
    return F.conv1d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''