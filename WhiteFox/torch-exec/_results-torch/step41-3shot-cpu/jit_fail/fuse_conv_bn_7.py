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
        c = torch.nn.Conv2d(3, 32, kernel_size=1, padding=0)
        torch.manual_seed(5)
        c.weight = torch.nn.Parameter(torch.ones(c.weight.size()), requires_grad=False)
        self.conv1 = c
        self.relu1 = torch.nn.ReLU()
        self.conv2 = c
        self.relu2 = torch.nn.ReLU()

    def forward(self, x):
        x = self.conv1(x)
        x = self.relu1(x)
        x = self.conv2(x)
        return self.relu2(x)



func = Model().to('cpu')


x = torch.randn(4, 3, 3, 3)

test_inputs = [x]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [32, 3, 1, 1], expected input[4, 32, 3, 3] to have 3 channels, but got 32 channels instead

jit:
Failed running call_function <built-in method conv2d of type object at 0x7bc74ef96ec0>(*(FakeTensor(..., size=(4, 32, 3, 3)), Parameter(FakeTensor(..., size=(32, 3, 1, 1))), Parameter(FakeTensor(..., size=(32,), requires_grad=True)), (1, 1), (0, 0), (1, 1), 1), **{}):
Given groups=1, weight of size [32, 3, 1, 1], expected input[4, 32, 3, 3] to have 3 channels, but got 32 channels instead

from user code:
   File "<string>", line 28, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 554, in forward
    return self._conv_forward(input, self.weight, self.bias)
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 549, in _conv_forward
    return F.conv2d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''