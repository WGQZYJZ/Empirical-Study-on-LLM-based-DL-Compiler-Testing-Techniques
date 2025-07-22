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
        self.conv_transpose_0 = torch.nn.Conv2d(4, 4, 3, stride=2, padding=1, bias=False)
        self.relu_1 = torch.nn.ReLU()
        self.conv_transpose_2 = torch.nn.ConvTranspose2d(4, 1, 3, stride=2, padding=1, output_padding=1, bias=False)
        self.relu_3 = torch.nn.ReLU()
        self.conv_transpose_4 = torch.nn.ConvTranspose2d(1, 1, 3, stride=2, padding=1, output_padding=1)

    def forward(self, x1):
        v1 = torch.transpose(x1, -3, -1)
        v2 = torch.transpose(x1, -2, -1)
        v3 = v1[:]
        v4 = self.conv_transpose_0(v3)
        v5 = v2[:]
        v6 = self.relu_1(v4)
        v7 = self.conv_transpose_2(v5)
        v8 = v3[:]
        v9 = self.relu_3(v7)
        v10 = self.conv_transpose_4(v8)
        v11 = torch.transpose(v10, -3, -1)
        v12 = torch.transpose(v11, -2, -1)
        v13 = torch.transpose(v12, -1, -3)
        return v13



func = Model().to('cpu')


x1 = torch.randn(1, 4, 6, 6)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [4, 4, 3, 3], expected input[1, 6, 6, 4] to have 4 channels, but got 6 channels instead

jit:
Failed running call_function <built-in method conv2d of type object at 0x7ea74dd96ec0>(*(FakeTensor(..., size=(1, 6, 6, 4)), Parameter(FakeTensor(..., size=(4, 4, 3, 3), requires_grad=True)), None, (2, 2), (1, 1), (1, 1), 1), **{}):
Given groups=1, weight of size [4, 4, 3, 3], expected input[1, 6, 6, 4] to have 4 channels, but got 6 channels instead

from user code:
   File "<string>", line 27, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 554, in forward
    return self._conv_forward(input, self.weight, self.bias)
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 549, in _conv_forward
    return F.conv2d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''