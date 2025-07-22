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
        self.conv_transpose = torch.nn.ConvTranspose2d(3, 6, 3, stride=[2, 2], padding=[28, 29], dilation=[2, 2])

    def forward(self, x1):
        v1 = self.conv_transpose(x1)
        v2 = torch.tanh(v1)
        return v2



func = Model().to('cpu')


x1 = torch.randn(1, 3, 1, 1)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given input size per channel: (1 x 1). Calculated output size per channel: (-51 x -53). Output size is too small

jit:
Failed running call_function <built-in method conv_transpose2d of type object at 0x71ac1f796ec0>(*(FakeTensor(..., size=(1, 3, 1, 1)), Parameter(FakeTensor(..., size=(3, 6, 3, 3), requires_grad=True)), Parameter(FakeTensor(..., size=(6,), requires_grad=True)), (2, 2), (28, 29), (0, 0), 1, (2, 2)), **{}):
Trying to create tensor with negative dimension -51: [1, 6, -51, -53]

from user code:
   File "<string>", line 20, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 1162, in forward
    return F.conv_transpose2d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''