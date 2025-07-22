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
        self.conv1 = torch.nn.Conv2d(3, 9, (13, 13), 1, (0, 1))
        self.conv2 = torch.nn.Conv2d(9, 3, (13, 13), 1, (1, 5))
        self.conv3 = torch.nn.Conv2d(3, 3, (13, 13), 1, (0, 2))

    def forward(self, x2):
        v1 = torch.sigmoid(self.conv1(x2))
        v3 = torch.sigmoid(self.conv2(v1))
        v5 = torch.sigmoid(self.conv3(x2))
        return None



func = Model().to('cuda')


x2 = torch.randn(1, 3, 9, 28)

test_inputs = [x2]

# JIT_FAIL
'''
direct:
Calculated padded input size per channel: (9 x 30). Kernel size: (13 x 13). Kernel size can't be greater than actual input size

jit:
Failed running call_function <built-in method conv2d of type object at 0x770cca596ec0>(*(FakeTensor(..., device='cuda:0', size=(1, 3, 9, 28)), Parameter(FakeTensor(..., device='cuda:0', size=(9, 3, 13, 13), requires_grad=True)), Parameter(FakeTensor(..., device='cuda:0', size=(9,), requires_grad=True)), (1, 1), (0, 1), (1, 1), 1), **{}):
Calculated padded input size per channel: (9 x 30). Kernel size: (13 x 13). Kernel size can't be greater than actual input size

from user code:
   File "<string>", line 22, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 554, in forward
    return self._conv_forward(input, self.weight, self.bias)
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 549, in _conv_forward
    return F.conv2d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''