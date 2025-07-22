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

class ModelTanh(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.conv_1 = torch.nn.Conv2d(in_channels=3, out_channels=1, kernel_size=(1, 203), stride=(1, 1), padding=(0, 0), dilation=(1, 1))

    def forward(self, input):
        X0 = self.conv_1(input)
        X1 = torch.tanh(X0)
        return X1



func = ModelTanh().to('cpu')


input = torch.randn(1, 3, 253, 1)

test_inputs = [input]

# JIT_FAIL
'''
direct:
Calculated padded input size per channel: (253 x 1). Kernel size: (1 x 203). Kernel size can't be greater than actual input size

jit:
Failed running call_function <built-in method conv2d of type object at 0x783c95b96ec0>(*(FakeTensor(..., size=(1, 3, 253, 1)), Parameter(FakeTensor(..., size=(1, 3, 1, 203), requires_grad=True)), Parameter(FakeTensor(..., size=(1,), requires_grad=True)), (1, 1), (0, 0), (1, 1), 1), **{}):
Calculated padded input size per channel: (253 x 1). Kernel size: (1 x 203). Kernel size can't be greater than actual input size

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