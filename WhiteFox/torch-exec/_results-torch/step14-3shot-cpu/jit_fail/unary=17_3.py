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
        self.conv2d = torch.nn.ConvTranspose2d(2, 2, 3, bias=True)
        self.conv2d_1 = torch.nn.ConvTranspose2d(5, 2, kernel_size=(5, 3), bias=False)
        self.conv2d_2 = torch.nn.ConvTranspose2d(4, 5, kernel_size=(2, 4), stride=(1, 2), bias=None)

    def forward(self, x1):
        v1 = self.conv2d(x1)
        v2 = v1.detach()
        v3 = self.conv2d_1(v2)
        v4 = self.conv2d_2(v1)
        v5 = v4.detach()
        return v5



func = Model().to('cpu')


x1 = torch.randn(7, 4, 20, 10)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given transposed=1, weight of size [2, 2, 3, 3], expected input[7, 4, 20, 10] to have 2 channels, but got 4 channels instead

jit:
Failed running call_function <built-in method conv_transpose2d of type object at 0x7d7027d96ec0>(*(FakeTensor(..., size=(7, 4, 20, 10)), Parameter(FakeTensor(..., size=(2, 2, 3, 3), requires_grad=True)), Parameter(FakeTensor(..., size=(2,), requires_grad=True)), (1, 1), (0, 0), (0, 0), 1, (1, 1)), **{}):
Given transposed=1, weight of size [2, 2, 3, 3], expected input[7, 4, 20, 10] to have 2 channels, but got 4 channels instead

from user code:
   File "<string>", line 22, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 1162, in forward
    return F.conv_transpose2d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''