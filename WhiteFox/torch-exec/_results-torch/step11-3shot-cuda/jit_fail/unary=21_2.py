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
        self.conv1 = torch.nn.Conv2d(10, 20, 2, stride=1, padding=0)
        self.conv2 = torch.nn.Conv2d(3, 20, 1, stride=1, padding=0)
        self.conv3 = torch.nn.Conv2d(20, 5, 4, stride=1, padding=0)
        self.conv4 = torch.nn.Conv2d(5, 10, 6, stride=1, padding=0)

    def forward(self, x):
        t1 = self.conv1(x)
        t2 = self.conv2(x)
        t3 = self.conv3(t1 + t2)
        t4 = self.conv4(t3)
        return t4



func = ModelTanh().to('cuda')


x = torch.randn(1, 10, 256, 256)

test_inputs = [x]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [20, 3, 1, 1], expected input[1, 10, 256, 256] to have 3 channels, but got 10 channels instead

jit:
Failed running call_function <built-in method conv2d of type object at 0x7fcf82996ec0>(*(FakeTensor(..., device='cuda:0', size=(1, 10, 256, 256)), Parameter(FakeTensor(..., device='cuda:0', size=(20, 3, 1, 1), requires_grad=True)), Parameter(FakeTensor(..., device='cuda:0', size=(20,), requires_grad=True)), (1, 1), (0, 0), (1, 1), 1), **{}):
Given groups=1, weight of size [20, 3, 1, 1], expected input[1, 10, 256, 256] to have 3 channels, but got 10 channels instead

from user code:
   File "<string>", line 24, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 554, in forward
    return self._conv_forward(input, self.weight, self.bias)
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 549, in _conv_forward
    return F.conv2d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''