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

class A(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(4, 5, kernel_size=5)

    def forward(self, input):
        y = self.conv(input)
        t = input.permute(1, 0, 2, 3)
        z = t.reshape((1, 20))
        x = y + z
        out = torch.rand_like(x)
        return out



func = A().to('cpu')


input = torch.randn(1, 3, 256, 256)

test_inputs = [input]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [5, 4, 5, 5], expected input[1, 3, 256, 256] to have 4 channels, but got 3 channels instead

jit:
Failed running call_function <built-in method conv2d of type object at 0x721309596ec0>(*(FakeTensor(..., size=(1, 3, 256, 256)), Parameter(FakeTensor(..., size=(5, 4, 5, 5), requires_grad=True)), Parameter(FakeTensor(..., size=(5,), requires_grad=True)), (1, 1), (0, 0), (1, 1), 1), **{}):
Given groups=1, weight of size [5, 4, 5, 5], expected input[1, 3, 256, 256] to have 4 channels, but got 3 channels instead

from user code:
   File "<string>", line 20, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 554, in forward
    return self._conv_forward(input, self.weight, self.bias)
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 549, in _conv_forward
    return F.conv2d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''