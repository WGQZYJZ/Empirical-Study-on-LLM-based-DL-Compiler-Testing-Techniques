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
        self.conv = torch.nn.Conv2d(5, 16, kernel_size=(5,), stride=(2,))

    def forward(self, x):
        v1 = self.conv(x)
        mask = v1 > 0
        v2 = v1 * 0.1
        v3 = torch.where(mask, v1, v2)
        return v3



func = Model().to('cpu')


x1 = torch.randn(1, 5, 40, 80)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
expected padding to be a single integer value or a list of 1 values to match the convolution dimensions, but got padding=[0, 0]

jit:
Failed running call_function <built-in method conv2d of type object at 0x7cacf6996ec0>(*(FakeTensor(..., size=(1, 5, s1, s2)), Parameter(FakeTensor(..., size=(16, 5, 5), requires_grad=True)), Parameter(FakeTensor(..., size=(16,), requires_grad=True)), (2,), (0, 0), (1, 1), 1), **{}):
tuple index out of range

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