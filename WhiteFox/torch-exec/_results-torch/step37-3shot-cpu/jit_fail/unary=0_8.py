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
        self.conv = torch.nn.Conv2d(62, 29, 23, stride=2, padding=2)
        self.dropout = torch.nn.Dropout(p=0.27975041001800915)
        self.relu = torch.nn.ReLU()

    def forward(self, x):
        v1 = self.conv(x)
        v2 = self.dropout(v1)
        v3 = v2 * 0.7678297169611875
        v4 = v2 * v2
        v5 = v4 * v2
        v6 = v5 * 0.2982368326428082
        v7 = v3 + v6
        v8 = v7 * 0.7860601645176003
        v9 = self.relu(v8)
        return v9



func = Model().to('cpu')


x = torch.randn(1, 62, 11, 11)

test_inputs = [x]

# JIT_FAIL
'''
direct:
Calculated padded input size per channel: (15 x 15). Kernel size: (23 x 23). Kernel size can't be greater than actual input size

jit:
Failed running call_function <built-in method conv2d of type object at 0x7acbfa996ec0>(*(FakeTensor(..., size=(1, 62, 11, 11)), Parameter(FakeTensor(..., size=(29, 62, 23, 23), requires_grad=True)), Parameter(FakeTensor(..., size=(29,), requires_grad=True)), (2, 2), (2, 2), (1, 1), 1), **{}):
Calculated padded input size per channel: (15 x 15). Kernel size: (23 x 23). Kernel size can't be greater than actual input size

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