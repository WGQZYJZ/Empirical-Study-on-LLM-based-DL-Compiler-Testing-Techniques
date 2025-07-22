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

class Module1(torch.nn.Module):

    def __init__(self):
        super(Module1, self).__init__()
        self.conv2d = torch.nn.Conv2d(3, 8, (3, 3), stride=(1, 1), padding=(1, 1), dilation=(1, 1), groups=1, bias=False)
        self.batchnorm2d = torch.nn.BatchNorm2d(8)

    def forward(self, x1):
        y1 = self.conv2d(x1)
        y2 = self.batchnorm2d(y1)
        return y2



func = Module1().to('cpu')


x1 = torch.randn(1, 6, 4, 4)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [8, 3, 3, 3], expected input[1, 6, 4, 4] to have 3 channels, but got 6 channels instead

jit:
Failed running call_function <built-in method conv2d of type object at 0x7c8ade196ec0>(*(FakeTensor(..., size=(1, 6, 4, 4)), Parameter(FakeTensor(..., size=(8, 3, 3, 3), requires_grad=True)), None, (1, 1), (1, 1), (1, 1), 1), **{}):
Given groups=1, weight of size [8, 3, 3, 3], expected input[1, 6, 4, 4] to have 3 channels, but got 6 channels instead

from user code:
   File "<string>", line 21, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 554, in forward
    return self._conv_forward(input, self.weight, self.bias)
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 549, in _conv_forward
    return F.conv2d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''