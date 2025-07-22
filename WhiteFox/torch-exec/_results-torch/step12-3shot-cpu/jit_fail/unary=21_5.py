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
        kernel_size = 9616
        input_dim = 3
        output_dim = 97
        stride = 4
        padding = 142
        self.conv = torch.nn.Conv1d(input_dim, output_dim, kernel_size, stride=stride, padding=padding)

    def forward(self, x):
        y1 = self.conv(x)
        y2 = torch.tanh(y1)
        return y2



func = ModelTanh().to('cpu')


x = torch.randn(20, 3, 2570)

test_inputs = [x]

# JIT_FAIL
'''
direct:
Calculated padded input size per channel: (2854). Kernel size: (9616). Kernel size can't be greater than actual input size

jit:
Failed running call_function <built-in method conv1d of type object at 0x703513996ec0>(*(FakeTensor(..., size=(20, 3, 2570)), Parameter(FakeTensor(..., size=(97, 3, 9616), requires_grad=True)), Parameter(FakeTensor(..., size=(97,), requires_grad=True)), (4,), (142,), (1,), 1), **{}):
Trying to create tensor with negative dimension -1690: [20, 97, -1690]

from user code:
   File "<string>", line 25, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 375, in forward
    return self._conv_forward(input, self.weight, self.bias)
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 370, in _conv_forward
    return F.conv1d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''