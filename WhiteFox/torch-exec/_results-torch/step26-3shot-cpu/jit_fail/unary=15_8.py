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
        self.conv1 = torch.nn.Conv2d(3, 32, 5, stride=1, padding=[1, 2, 3, 4])

    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = torch.relu(v1)
        return v2



func = Model().to('cpu')


x1 = torch.randn(3, 3, 100, 100)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
expected padding to be a single integer value or a list of 2 values to match the convolution dimensions, but got padding=[1, 2, 3, 4]

jit:
Failed running call_function <built-in method conv2d of type object at 0x7d9509196ec0>(*(FakeTensor(..., size=(3, 3, 100, 100)), Parameter(FakeTensor(..., size=(32, 3, 5, 5), requires_grad=True)), Parameter(FakeTensor(..., size=(32,), requires_grad=True)), (1, 1), (1, 2, 3, 4), (1, 1), 1), **{}):
expected padding to be a single integer value or a list of 2 values to match the convolution dimensions, but got padding=[1, 2, 3, 4]

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