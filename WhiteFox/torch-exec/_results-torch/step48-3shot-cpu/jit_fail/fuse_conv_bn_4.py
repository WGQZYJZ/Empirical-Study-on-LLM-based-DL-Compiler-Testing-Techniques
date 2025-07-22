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

    def __init__(self, conv_dim):
        super().__init__()
        self.layers = [torch.nn.Conv2d(3, conv_dim, conv_dim), torch.nn.BatchNorm2d(conv_dim)]
        for _ in range(10):
            self.layers.append(torch.nn.ReLU())
            self.layers.append(torch.nn.Conv2d(conv_dim, conv_dim, conv_dim))
            self.layers.append(torch.nn.BatchNorm2d(conv_dim))

    def forward(self, x):
        for layer in self.layers:
            x = layer(x)
        return x


conv_dim = 10

func = Model(conv_dim).to('cpu')


x = torch.randn(1, 3, 6, 6)

test_inputs = [x]

# JIT_FAIL
'''
direct:
Calculated padded input size per channel: (6 x 6). Kernel size: (10 x 10). Kernel size can't be greater than actual input size

jit:
Failed running call_function <built-in method conv2d of type object at 0x7a2c67d96ec0>(*(FakeTensor(..., size=(1, 3, 6, 6)), Parameter(FakeTensor(..., size=(10, 3, 10, 10), requires_grad=True)), Parameter(FakeTensor(..., size=(10,), requires_grad=True)), (1, 1), (0, 0), (1, 1), 1), **{}):
Calculated padded input size per channel: (6 x 6). Kernel size: (10 x 10). Kernel size can't be greater than actual input size

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