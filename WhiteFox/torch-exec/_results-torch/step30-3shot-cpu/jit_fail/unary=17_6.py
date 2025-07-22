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
        self.conv = torch.nn.ConvTranspose2d(50, 100, 2, stride=2)
        self.conv1 = torch.nn.ConvTranspose2d(100, 25, 2, stride=1)
        self.conv2 = torch.nn.ConvTranspose2d(25, 75, 3, stride=1)

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = self.conv1(v1)
        v3 = self.conv2(v2)
        return v3



func = Model().to('cpu')


x1 = torch.randn(1, 1, 140, 1)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given transposed=1, weight of size [50, 100, 2, 2], expected input[1, 1, 140, 1] to have 50 channels, but got 1 channels instead

jit:
Failed running call_function <built-in method conv_transpose2d of type object at 0x73310fd96ec0>(*(FakeTensor(..., size=(1, 1, 140, 1)), Parameter(FakeTensor(..., size=(50, 100, 2, 2), requires_grad=True)), Parameter(FakeTensor(..., size=(100,), requires_grad=True)), (2, 2), (0, 0), (0, 0), 1, (1, 1)), **{}):
Given transposed=1, weight of size [50, 100, 2, 2], expected input[1, 1, 140, 1] to have 50 channels, but got 1 channels instead

from user code:
   File "<string>", line 22, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 1162, in forward
    return F.conv_transpose2d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''