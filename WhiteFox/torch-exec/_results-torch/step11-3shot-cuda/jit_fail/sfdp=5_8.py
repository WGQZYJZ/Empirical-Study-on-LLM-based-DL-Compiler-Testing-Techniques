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
        self.key = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.query = torch.nn.Conv2d(8, 8, 1, stride=1, padding=1)
        self.value = torch.nn.Conv2d(8, 8, 1, stride=1, padding=1)

    def forward(self, x1):
        y1 = self.query(x1)
        y2 = self.key(x1)
        y3 = y2.transpose(-2, -1)
        y4 = torch.matmul(y1, y3)
        y5 = y4 / math.sqrt(8)
        y6 = y3 + 1
        v1 = torch.softmax(y6, dim=1)
        y7 = self.value(x1)
        v2 = v1 @ y7
        return v2


func = Model().to('cuda')


x1 = torch.randn(1, 3, 64, 64)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [8, 8, 1, 1], expected input[1, 3, 64, 64] to have 8 channels, but got 3 channels instead

jit:
Failed running call_function <built-in method conv2d of type object at 0x7f11d5196ec0>(*(FakeTensor(..., device='cuda:0', size=(1, 3, 64, 64)), Parameter(FakeTensor(..., device='cuda:0', size=(8, 8, 1, 1), requires_grad=True)), Parameter(FakeTensor(..., device='cuda:0', size=(8,), requires_grad=True)), (1, 1), (1, 1), (1, 1), 1), **{}):
Given groups=1, weight of size [8, 8, 1, 1], expected input[1, 3, 64, 64] to have 8 channels, but got 3 channels instead

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