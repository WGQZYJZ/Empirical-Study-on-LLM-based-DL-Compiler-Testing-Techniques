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
        torch.manual_seed(1)
        self.layer = torch.nn.Sequential(torch.nn.Conv3d(3, 4, 2, bias=True), torch.nn.Conv3d(3, 5, 3, bias=False))

    def forward(self, x2):
        s = self.layer(x2)
        return s



func = Model().to('cpu')


x2 = torch.randn(1, 3, 4, 4, 4)

test_inputs = [x2]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [5, 3, 3, 3, 3], expected input[1, 4, 3, 3, 3] to have 3 channels, but got 4 channels instead

jit:
Failed running call_function <built-in method conv3d of type object at 0x747cb4b96ec0>(*(FakeTensor(..., size=(1, 4, 3, 3, 3)), Parameter(FakeTensor(..., size=(5, 3, 3, 3, 3), requires_grad=True)), None, (1, 1, 1), (0, 0, 0), (1, 1, 1), 1), **{}):
Given groups=1, weight of size [5, 3, 3, 3, 3], expected input[1, 4, 3, 3, 3] to have 3 channels, but got 4 channels instead

from user code:
   File "<string>", line 21, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/container.py", line 250, in forward
    input = module(input)
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 725, in forward
    return self._conv_forward(input, self.weight, self.bias)
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 720, in _conv_forward
    return F.conv3d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''