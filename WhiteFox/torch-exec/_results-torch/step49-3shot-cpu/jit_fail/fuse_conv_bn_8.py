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
        self.conv1 = torch.nn.Conv1d(3, 5, 7)
        self.bn1 = torch.nn.BatchNorm1d(3)
        self.conv2 = torch.nn.Conv2d(1, 10, 7)
        self.bn2 = torch.nn.BatchNorm2d(1)

    def forward(self, x3, x1):
        y3 = self.conv1(x3.clone())
        y3 = self.bn1(y3.clone())
        y1 = self.conv2(x1.clone())
        y1 = self.bn2(y1.clone())
        return (y3.view(-1), y1.view(-1))



func = Model().to('cpu')


x3 = torch.randn(1, 3, 10, 10)

x1 = torch.randn(1, 1, 8, 8)

test_inputs = [x3, x1]

# JIT_FAIL
'''
direct:
Expected 2D (unbatched) or 3D (batched) input to conv1d, but got input of size: [1, 3, 10, 10]

jit:
Failed running call_function <built-in method conv1d of type object at 0x7d0e3ff96ec0>(*(FakeTensor(..., size=(1, 3, 10, 10)), Parameter(FakeTensor(..., size=(5, 3, 7), requires_grad=True)), Parameter(FakeTensor(..., size=(5,), requires_grad=True)), (1,), (0,), (1,), 1), **{}):
Expected 2D (unbatched) or 3D (batched) input to conv1d, but got input of size: [1, 3, 10, 10]

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