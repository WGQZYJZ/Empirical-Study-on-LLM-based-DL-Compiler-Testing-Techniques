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
        self.conv = torch.nn.Conv2d(4, 4, 2)
        self.conv1 = torch.nn.Conv2d(4, 4, 2)
        self.conv2 = torch.nn.ConvTranspose2d(4, 4, 2)
        self.fc = torch.nn.Linear(4, 1)

    def forward(self, x):
        x = self.conv(x)
        z = self.conv1(x)
        z = torch.mean(z, dim=1, keepdim=True)
        x = torch.transpose(x, 1, 2)
        x = self.conv2(x, output_size=(z, x.shape[2]))
        x = torch.transpose(x, 1, 2)
        return x



func = Model().to('cpu')


x = torch.randn(1, 1, 8, 8)

test_inputs = [x]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [4, 4, 2, 2], expected input[1, 1, 8, 8] to have 4 channels, but got 1 channels instead

jit:
Failed running call_function <built-in method conv2d of type object at 0x799ff0796ec0>(*(FakeTensor(..., size=(1, 1, 8, 8)), Parameter(FakeTensor(..., size=(4, 4, 2, 2), requires_grad=True)), Parameter(FakeTensor(..., size=(4,), requires_grad=True)), (1, 1), (0, 0), (1, 1), 1), **{}):
Given groups=1, weight of size [4, 4, 2, 2], expected input[1, 1, 8, 8] to have 4 channels, but got 1 channels instead

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