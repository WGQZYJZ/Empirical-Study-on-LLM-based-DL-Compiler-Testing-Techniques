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
        self.conv = torch.nn.Conv2d(3, 4, 1, padding=1)
        self.convs = torch.nn.Conv2d(4, 5, (3, 5), padding=1)
        self.conv2 = torch.nn.Conv2d(5, 6, (2, 8), padding=2)
        self.conv3 = torch.nn.Conv2d(6, 7, 1, padding=1)
        self.conv4 = torch.nn.Conv2d(7, 6, 7, padding=3)
        self.conv5 = torch.nn.Conv2d(6, 5, 1, padding=2)
        self.conv6 = torch.nn.Conv2d(5, 4, 7, padding=5)
        self.conv7 = torch.nn.Conv2d(4, 3, 1, padding=2)
        self.conv8 = torch.nn.Conv2d(3, 2, (3, 2), padding=3)
        self.conv9 = torch.nn.Conv2d(2, 1, 7, padding=8)
        self.tanh = torch.nn.Tanh()

    def forward(self, x):
        v1 = self.conv(x)
        v2 = torch.tanh(v1)
        v3 = self.convs(v2)
        v4 = self.conv2(v3)
        v5 = self.conv3(v4)
        v6 = torch.tanh(v5)
        v7 = self.conv4(v6)
        v8 = self.conv5(v7)
        v9 = self.conv6(v8)
        v10 = torch.tanh(v9)
        v11 = self.conv7(v10)
        v12 = self.conv8(v11)
        v13 = self.conv9(v12)
        v14 = torch.tanh(v13)
        return v14



func = ModelTanh().to('cpu')


x = torch.randn(3, 5, 5, 8)

test_inputs = [x]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [4, 3, 1, 1], expected input[3, 5, 5, 8] to have 3 channels, but got 5 channels instead

jit:
Failed running call_function <built-in method conv2d of type object at 0x74746f196ec0>(*(FakeTensor(..., size=(3, 5, 5, 8)), Parameter(FakeTensor(..., size=(4, 3, 1, 1), requires_grad=True)), Parameter(FakeTensor(..., size=(4,), requires_grad=True)), (1, 1), (1, 1), (1, 1), 1), **{}):
Given groups=1, weight of size [4, 3, 1, 1], expected input[3, 5, 5, 8] to have 3 channels, but got 5 channels instead

from user code:
   File "<string>", line 30, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 554, in forward
    return self._conv_forward(input, self.weight, self.bias)
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 549, in _conv_forward
    return F.conv2d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''