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
        self.conv_transpose = torch.nn.ConvTranspose2d(30, 43, kernel_size=7, stride=1, padding=12)

    def forward(self, x1):
        v1 = self.conv_transpose(x1)
        v2 = v1 * 0.5
        v3 = v1 * 0.7071067811865476
        v4 = torch.erf(v3)
        v5 = v4 + 1
        v6 = v2 * v5
        return v6



func = Model().to('cpu')


x1 = torch.randn(1, 30, 6, 6)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
could not construct a memory descriptor using a format tag

jit:
Failed running call_function <built-in method conv_transpose2d of type object at 0x78e852d96ec0>(*(FakeTensor(..., size=(1, 30, s1, s2)), Parameter(FakeTensor(..., size=(30, 43, 7, 7), requires_grad=True)), Parameter(FakeTensor(..., size=(43,), requires_grad=True)), (1, 1), (12, 12), (0, 0), 1, (1, 1)), **{}):
Trying to create tensor with negative dimension s1 - 18: [1, 43, s1 - 18, s2 - 18]

from user code:
   File "<string>", line 20, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 1162, in forward
    return F.conv_transpose2d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''