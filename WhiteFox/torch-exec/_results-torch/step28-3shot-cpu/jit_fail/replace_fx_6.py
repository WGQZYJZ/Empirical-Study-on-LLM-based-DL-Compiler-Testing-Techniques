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

class model(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(2, 16, (5, 5), 1, (2, 2))
        self.dropout1 = torch.nn.Dropout(0.2)
        self.dropout2 = torch.nn.Dropout(0.4)

    def forward(self, input):
        x = self.conv(input)
        x = self.dropout1(x)
        x = self.dropout2(x)
        x = torch.rand_like(x)
        return x



func = model().to('cpu')


x1 = torch.randn(1, 88, 88, 2)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [16, 2, 5, 5], expected input[1, 88, 88, 2] to have 2 channels, but got 88 channels instead

jit:
Failed running call_function <built-in method conv2d of type object at 0x77d2f4996ec0>(*(FakeTensor(..., size=(1, 88, 88, 2)), Parameter(FakeTensor(..., size=(16, 2, 5, 5), requires_grad=True)), Parameter(FakeTensor(..., size=(16,), requires_grad=True)), (1, 1), (2, 2), (1, 1), 1), **{}):
Given groups=1, weight of size [16, 2, 5, 5], expected input[1, 88, 88, 2] to have 2 channels, but got 88 channels instead

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