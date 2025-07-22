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
        self.Conv2d = torch.nn.Conv2d(2, 3, 1)
        self.ConvTranspose2d = torch.nn.ConvTranspose2d(3, 3, 1, stride=1, output_padding=0)

    def forward(self, x1):
        v1 = self.Conv2d(x1)
        v2 = v1 * 0.5
        v3 = v1 * v1 * v1
        v4 = v3 * 0.044715
        v5 = v1 + v4
        v6 = v5 * 0.7978845608028654
        v7 = torch.tanh(v6)
        v20 = self.ConvTranspose2d(x1)
        v8 = v7 + 1
        v9 = v2 * v8
        return v9



func = Model().to('cpu')


x1 = torch.randn(2, 2, 2, 2)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given transposed=1, weight of size [3, 3, 1, 1], expected input[2, 2, 2, 2] to have 3 channels, but got 2 channels instead

jit:
Failed running call_function <built-in method conv_transpose2d of type object at 0x79c000b96ec0>(*(FakeTensor(..., size=(2, 2, 2, 2)), Parameter(FakeTensor(..., size=(3, 3, 1, 1), requires_grad=True)), Parameter(FakeTensor(..., size=(3,), requires_grad=True)), (1, 1), (0, 0), (0, 0), 1, (1, 1)), **{}):
Given transposed=1, weight of size [3, 3, 1, 1], expected input[2, 2, 2, 2] to have 3 channels, but got 2 channels instead

from user code:
   File "<string>", line 28, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 1162, in forward
    return F.conv_transpose2d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''