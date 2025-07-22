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

class ModelTanh(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 11, 1)
        self.conv2 = torch.nn.Conv2d(3, 19, 1, padding=1)

    def forward(self, x):
        t1 = self.conv1(x)
        t2 = torch.tanh(t1)
        t3 = self.conv2(t2)
        t4 = torch.tanh(t3)
        return t4



func = ModelTanh().to('cpu')


x = torch.randn(1, 3, 28, 28)

test_inputs = [x]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [19, 3, 1, 1], expected input[1, 11, 28, 28] to have 3 channels, but got 11 channels instead

jit:
Failed running call_function <built-in method conv2d of type object at 0x7aa784996ec0>(*(FakeTensor(..., size=(1, 11, 28, 28)), Parameter(FakeTensor(..., size=(19, 3, 1, 1), requires_grad=True)), Parameter(FakeTensor(..., size=(19,), requires_grad=True)), (1, 1), (1, 1), (1, 1), 1), **{}):
Given groups=1, weight of size [19, 3, 1, 1], expected input[1, 11, 28, 28] to have 3 channels, but got 11 channels instead

from user code:
   File "<string>", line 23, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 554, in forward
    return self._conv_forward(input, self.weight, self.bias)
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 549, in _conv_forward
    return F.conv2d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''