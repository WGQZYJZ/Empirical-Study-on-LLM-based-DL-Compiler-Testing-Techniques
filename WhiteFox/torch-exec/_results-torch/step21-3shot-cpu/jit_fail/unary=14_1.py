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
        self.conv_transpose_5 = torch.nn.ConvTranspose2d(6, 3, 2, stride=2, padding=24)

    def forward(self, x1):
        v1 = self.conv_transpose_5(x1)
        v2 = torch.sigmoid(v1)
        v3 = v1 * v2
        return v3



func = Model().to('cpu')


x1 = torch.randn(1, 6, 14, 14)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given input size per channel: (14 x 14). Calculated output size per channel: (-20 x -20). Output size is too small

jit:
Failed running call_function <built-in method conv_transpose2d of type object at 0x77f6fd996ec0>(*(FakeTensor(..., size=(1, 6, s1, s2)), Parameter(FakeTensor(..., size=(6, 3, 2, 2), requires_grad=True)), Parameter(FakeTensor(..., size=(3,), requires_grad=True)), (2, 2), (24, 24), (0, 0), 1, (1, 1)), **{}):
Trying to create tensor with negative dimension 2*s1 - 48: [1, 3, 2*s1 - 48, 2*s2 - 48]

from user code:
   File "<string>", line 20, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 1162, in forward
    return F.conv_transpose2d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''