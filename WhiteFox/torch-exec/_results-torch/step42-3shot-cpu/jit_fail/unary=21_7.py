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

class ModuleTest(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv3d(in_channels=1, out_channels=2, stride=(1, 1), kernel_size=2)
        self.relu1 = torch.nn.ReLU6(inplace=False)

    def forward(self, x):
        conv1 = self.conv1(x)
        relu1 = self.relu1(conv1)
        return relu1



func = ModuleTest().to('cpu')


x = torch.randn(1, 1, 5, 5, 5)

test_inputs = [x]

# JIT_FAIL
'''
direct:
expected stride to be a single integer value or a list of 3 values to match the convolution dimensions, but got stride=[1, 1]

jit:
Failed running call_function <built-in method conv3d of type object at 0x710841796ec0>(*(FakeTensor(..., size=(1, 1, 5, 5, 5)), Parameter(FakeTensor(..., size=(2, 1, 2, 2, 2), requires_grad=True)), Parameter(FakeTensor(..., size=(2,), requires_grad=True)), (1, 1), (0, 0, 0), (1, 1, 1), 1), **{}):
expected stride to be a single integer value or a list of 3 values to match the convolution dimensions, but got stride=[1, 1]

from user code:
   File "<string>", line 21, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 725, in forward
    return self._conv_forward(input, self.weight, self.bias)
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 720, in _conv_forward
    return F.conv3d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''