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
        self.conv1 = torch.nn.ConvTranspose2d(1, 64, 3, stride=1, padding=1)
        self.conv2 = torch.nn.ConvTranspose2d(64, 128, 3, stride=2, padding=1)
        self.conv3 = torch.nn.ConvTranspose2d(128, 256, 3, stride=2, padding=1)
        self.conv4 = torch.nn.ConvTranspose2d(256, 3, 5, stride=3, padding=1)

    def forward(self, x):
        v1 = self.conv1(x)
        v2 = v1 - 1.5
        v3 = F.elu(v2, 0.5)
        v4 = v3 - 0.001
        v5 = self.conv2(v3)
        v6 = F.elu(v4, 1.5)
        v7 = v5 - 0.002
        v8 = self.conv3(v6)
        v9 = F.elu(v7, 2.0)
        v10 = v8 - 0.003
        v11 = self.conv4(v9)
        return v11



func = Model().to('cpu')


x = torch.randn(1, 1, 13, 13)

test_inputs = [x]

# JIT_FAIL
'''
direct:
Given transposed=1, weight of size [128, 256, 3, 3], expected input[1, 64, 13, 13] to have 128 channels, but got 64 channels instead

jit:
Failed running call_function <built-in method conv_transpose2d of type object at 0x75472b996ec0>(*(FakeTensor(..., size=(1, 64, 13, 13)), Parameter(FakeTensor(..., size=(128, 256, 3, 3), requires_grad=True)), Parameter(FakeTensor(..., size=(256,), requires_grad=True)), (2, 2), (1, 1), (0, 0), 1, (1, 1)), **{}):
Given transposed=1, weight of size [128, 256, 3, 3], expected input[1, 64, 13, 13] to have 128 channels, but got 64 channels instead

from user code:
   File "<string>", line 30, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 1162, in forward
    return F.conv_transpose2d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''