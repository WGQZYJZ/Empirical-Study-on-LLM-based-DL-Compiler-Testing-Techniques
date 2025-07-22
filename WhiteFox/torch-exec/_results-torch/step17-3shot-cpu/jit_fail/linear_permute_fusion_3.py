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
        self.conv = torch.nn.Conv2d(3, 2, [2, 2])

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1.permute([0, 2, 1, 3])
        return (v1, v2)



func = Model().to('cpu')


x1 = torch.randn((2, 2, 3, 3))

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [2, 3, 2, 2], expected input[2, 2, 3, 3] to have 3 channels, but got 2 channels instead

jit:
Failed running call_function <built-in method conv2d of type object at 0x7b7824596ec0>(*(FakeTensor(..., size=(s0, s1, s2, s3)), Parameter(FakeTensor(..., size=(2, 3, 2, 2), requires_grad=True)), Parameter(FakeTensor(..., size=(2,), requires_grad=True)), (1, 1), (0, 0), (1, 1), 1), **{}):
Given groups=1, weight of size [2, 3, 2, 2], expected input[s0, s1, s2, s3] to have 3 channels, but got s1 channels instead

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