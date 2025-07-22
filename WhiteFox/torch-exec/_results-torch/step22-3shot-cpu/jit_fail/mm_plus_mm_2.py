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
        super(Model, self).__init__()
        self.conv1 = torch.nn.Conv2d(1, 20, 5)
        self.conv2 = torch.nn.Conv2d(20, 20, 5)

    def forward(self, x):
        x = self.conv1(x)
        x = self.conv2(x)
        return x.nn.Conv2d(20, 20, 5)



func = Model().to('cpu')


x = torch.randn(5, 5, 5)

test_inputs = [x]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [20, 1, 5, 5], expected input[1, 5, 5, 5] to have 1 channels, but got 5 channels instead

jit:
Failed running call_function <built-in method conv2d of type object at 0x7c7ce5b96ec0>(*(FakeTensor(..., size=(5, 5, 5)), Parameter(FakeTensor(..., size=(20, 1, 5, 5), requires_grad=True)), Parameter(FakeTensor(..., size=(20,), requires_grad=True)), (1, 1), (0, 0), (1, 1), 1), **{}):
Given groups=1, weight of size [20, 1, 5, 5], expected input[1, 5, 5, 5] to have 1 channels, but got 5 channels instead

from user code:
   File "<string>", line 21, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 554, in forward
    return self._conv_forward(input, self.weight, self.bias)
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 549, in _conv_forward
    return F.conv2d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''