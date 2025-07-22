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
        self.conv = torch.nn.ConvTranspose2d(3, 16, 1)
        self.bn = torch.nn.BatchNorm2d(16)
        self.relu = torch.nn.ReLU()
        self.maxpool = torch.nn.MaxPool2d(3)

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = self.bn(v1)
        v3 = self.relu(v2)
        v4 = self.conv(v3)
        v5 = self.maxpool(v4)
        v6 = self.conv(v5)
        v7 = self.relu(v6)
        v8 = self.conv(v7)
        v9 = self.relu(v8)
        v10 = torch.sigmoid(v9)
        return v10



func = Model().to('cpu')


x1 = torch.randn(1, 3, 32, 32)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given transposed=1, weight of size [3, 16, 1, 1], expected input[1, 16, 32, 32] to have 3 channels, but got 16 channels instead

jit:
Failed running call_function <built-in method conv_transpose2d of type object at 0x77e60c396ec0>(*(FakeTensor(..., size=(1, 16, 32, 32)), Parameter(FakeTensor(..., size=(3, 16, 1, 1), requires_grad=True)), Parameter(FakeTensor(..., size=(16,), requires_grad=True)), (1, 1), (0, 0), (0, 0), 1, (1, 1)), **{}):
Given transposed=1, weight of size [3, 16, 1, 1], expected input[1, 16, 32, 32] to have 3 channels, but got 16 channels instead

from user code:
   File "<string>", line 26, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 1162, in forward
    return F.conv_transpose2d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''