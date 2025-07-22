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
        self.conv_transpose = torch.nn.ConvTranspose2d(7, 4, 5)

    def forward(self, x1):
        v1 = self.conv_transpose(x1)
        v2 = v1 * 0.5
        v3 = v1 * v1 * v1
        v4 = v3 * 0.044715
        v5 = v1 + v4
        v6 = v5 * 0.7978845608028654
        v7 = torch.tanh(v6)
        v8 = v7 + 1
        v9 = v2 * v8
        return v9



func = Model().to('cpu')


x1 = torch.randn(1, 5, 2, 12)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given transposed=1, weight of size [7, 4, 5, 5], expected input[1, 5, 2, 12] to have 7 channels, but got 5 channels instead

jit:
Failed running call_function <built-in method conv_transpose2d of type object at 0x72c361d96ec0>(*(FakeTensor(..., size=(1, s0, s1, s2)), Parameter(FakeTensor(..., size=(7, 4, 5, 5), requires_grad=True)), Parameter(FakeTensor(..., size=(4,), requires_grad=True)), (1, 1), (0, 0), (0, 0), 1, (1, 1)), **{}):
Given transposed=1, weight of size [7, 4, 5, 5], expected input[1, s0, s1, s2] to have 7 channels, but got s0 channels instead

from user code:
   File "<string>", line 20, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 1162, in forward
    return F.conv_transpose2d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''