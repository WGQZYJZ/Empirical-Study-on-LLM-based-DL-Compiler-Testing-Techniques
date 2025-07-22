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
        self.conv = torch.nn.Conv2d(16, 32, (3, 3), (2, 2), padding=1)

    def forward(self, x):
        v1 = self.conv(x)
        v2 = v1 * 0.75
        return v2



func = Model().to('cpu')



x = torch.randn(1, 16, 64, 64, dtype=torch.float16)

test_inputs = [x]

# JIT_FAIL
'''
direct:
Input type (c10::Half) and bias type (float) should be the same

jit:
Failed running call_function <built-in method conv2d of type object at 0x7a2521396ec0>(*(FakeTensor(..., size=(1, s0, 64, 64), dtype=torch.float16), Parameter(FakeTensor(..., size=(32, 16, 3, 3), requires_grad=True)), Parameter(FakeTensor(..., size=(32,), requires_grad=True)), (2, 2), (1, 1), (1, 1), 1), **{}):
Input type (c10::Half) and bias type (float) should be the same

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