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

class ModelNew1(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 2, 2)
        self.dropout = torch.nn.Dropout(0.1)
        self.conv2 = torch.nn.Conv2d(6, 2, 2)
        self.linear1 = torch.nn.Linear(2, 3)

    def forward(self, x):
        x = self.conv(x)
        x = self.dropout(x)
        x = self.conv2(x)
        x = torch.rand_like(x)
        x = torch.nn.functional.dropout(x)
        x = self.linear1(x)
        return x



func = ModelNew1().to('cpu')


x1 = torch.randn(2, 3, 2, 2)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [2, 6, 2, 2], expected input[2, 2, 1, 1] to have 6 channels, but got 2 channels instead

jit:
Failed running call_function <built-in method conv2d of type object at 0x77d2f4996ec0>(*(FakeTensor(..., size=(2, 2, 1, 1)), Parameter(FakeTensor(..., size=(2, 6, 2, 2), requires_grad=True)), Parameter(FakeTensor(..., size=(2,), requires_grad=True)), (1, 1), (0, 0), (1, 1), 1), **{}):
Given groups=1, weight of size [2, 6, 2, 2], expected input[2, 2, 1, 1] to have 6 channels, but got 2 channels instead

from user code:
   File "<string>", line 25, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 554, in forward
    return self._conv_forward(input, self.weight, self.bias)
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 549, in _conv_forward
    return F.conv2d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''