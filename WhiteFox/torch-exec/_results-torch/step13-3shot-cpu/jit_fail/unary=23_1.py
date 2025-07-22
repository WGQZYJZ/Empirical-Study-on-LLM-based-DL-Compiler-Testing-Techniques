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
        self.conv = torch.nn.ConvTranspose2d(35, 32, 3, stride=1, padding=2)
        self.conv = torch.nn.ConvTranspose2d(32, 96, 3, stride=1, padding=2)

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.tanh(v1)
        return v2



func = Model().to('cpu')


x1 = torch.randn(1, 35, 10, 10)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given transposed=1, weight of size [32, 96, 3, 3], expected input[1, 35, 10, 10] to have 32 channels, but got 35 channels instead

jit:
Failed running call_function <built-in method conv_transpose2d of type object at 0x7e0d41596ec0>(*(FakeTensor(..., size=(1, 35, 10, 10)), Parameter(FakeTensor(..., size=(32, 96, 3, 3), requires_grad=True)), Parameter(FakeTensor(..., size=(96,), requires_grad=True)), (1, 1), (2, 2), (0, 0), 1, (1, 1)), **{}):
Given transposed=1, weight of size [32, 96, 3, 3], expected input[1, 35, 10, 10] to have 32 channels, but got 35 channels instead

from user code:
   File "<string>", line 21, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 1162, in forward
    return F.conv_transpose2d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''