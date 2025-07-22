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
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.other_conv = torch.nn.Conv2d(8, 8, 9)

    def forward(self, input_tensor):
        t1 = self.conv(input_tensor)
        t2 = 3 + t1
        t3 = t2.clamp_(min=0, max=6)
        t4 = t3.div(6)
        t5 = t4.permute(0, 2, 3, 1)
        t6 = self.other_conv(t5)
        t7 = t6.clamp_max(6)
        t8 = t7.div(6)
        t9 = t8.permute(0, 3, 1, 2)
        t10 = t9.clamp_max(6)
        t11 = t10.div(6)
        return t11



func = Model().to('cpu')


input_tensor = torch.randn(3, 3, 64, 64)

test_inputs = [input_tensor]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [8, 8, 9, 9], expected input[3, 66, 66, 8] to have 8 channels, but got 66 channels instead

jit:
Failed running call_function <built-in method conv2d of type object at 0x756abc996ec0>(*(FakeTensor(..., size=(3, 66, 66, 8)), Parameter(FakeTensor(..., size=(8, 8, 9, 9), requires_grad=True)), Parameter(FakeTensor(..., size=(8,), requires_grad=True)), (1, 1), (0, 0), (1, 1), 1), **{}):
Given groups=1, weight of size [8, 8, 9, 9], expected input[3, 66, 66, 8] to have 8 channels, but got 66 channels instead

from user code:
   File "<string>", line 26, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 554, in forward
    return self._conv_forward(input, self.weight, self.bias)
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 549, in _conv_forward
    return F.conv2d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''