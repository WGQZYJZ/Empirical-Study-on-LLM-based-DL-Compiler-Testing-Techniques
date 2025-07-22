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
        self.conv_transpose64_no_stride = torch.nn.ConvTranspose2d(1, 3, 1, stride=1, padding=0)
        self.conv_transpose64_stride = torch.nn.ConvTranspose2d(1, 3, 1, stride=2, padding=0)

    def forward(self, x1, x2):
        v1 = self.conv_transpose64_no_stride(x1)
        v2 = self.conv_transpose64_stride(x2)
        v3 = torch.flatten(x1, 1)
        v4 = torch.flatten(x2, 1)
        v5 = torch.flatten(v1, 1)
        v6 = torch.flatten(v2, 1)
        return v1



func = Model().to('cpu')


x1 = torch.randn(1, 128, 16, 16)

x2 = torch.randn(1, 128, 32, 32)

test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
Given transposed=1, weight of size [1, 3, 1, 1], expected input[1, 128, 16, 16] to have 1 channels, but got 128 channels instead

jit:
Failed running call_function <built-in method conv_transpose2d of type object at 0x7579da196ec0>(*(FakeTensor(..., size=(1, 128, 16, 16)), Parameter(FakeTensor(..., size=(1, 3, 1, 1), requires_grad=True)), Parameter(FakeTensor(..., size=(3,), requires_grad=True)), (1, 1), (0, 0), (0, 0), 1, (1, 1)), **{}):
Given transposed=1, weight of size [1, 3, 1, 1], expected input[1, 128, 16, 16] to have 1 channels, but got 128 channels instead

from user code:
   File "<string>", line 21, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 1162, in forward
    return F.conv_transpose2d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''