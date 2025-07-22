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
        self.conv1 = nn.Conv2d(3, 32, kernel_size=(2, 2), stride=(2, 2), padding=0, bias=False)
        self.conv2 = nn.Conv2d(32, 32, kernel_size=(2, 2), stride=(1, 1), padding=0, bias=False)
        self.conv3 = nn.Conv2d(32, 28, kernel_size=(2, 2), stride=(2, 2), padding=0, bias=False)

    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = F.relu(v1)
        v3 = self.conv2(v2)
        v4 = F.relu(v3)
        v5 = self.conv3(v2)
        v6 = F.relu(v5)
        v7 = torch.tanh(v6)
        return v7



func = Model().to('cpu')


x1 = torch.randn(1, 3, 3, 3)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Calculated padded input size per channel: (1 x 1). Kernel size: (2 x 2). Kernel size can't be greater than actual input size

jit:
Failed running call_function <built-in method conv2d of type object at 0x70fb5b596ec0>(*(FakeTensor(..., size=(1, 32, (s1//2), (s2//2))), Parameter(FakeTensor(..., size=(32, 32, 2, 2), requires_grad=True)), None, (1, 1), (0, 0), (1, 1), 1), **{}):
Calculated padded input size per channel: ((s1//2) x (s2//2)). Kernel size: (2 x 2). Kernel size can't be greater than actual input size

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