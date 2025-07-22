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
        self.conv = torch.nn.ConvTranspose2d(3, 16, 2)
        self.conv1 = torch.nn.ConvTranspose2d(32, 64, (3, 3), 2)
        self.conv2 = torch.nn.ConvTranspose2d(64, 128, kernel_size=(2, 2), stride=(3, 3))

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.relu(v1)
        v3 = self.conv1(v1)
        v4 = self.conv2(v3)
        v4 = torch.sigmoid(v4)
        return v4



func = Model().to('cuda')


x1 = torch.randn(3, 3, 5, 5)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given transposed=1, weight of size [32, 64, 3, 3], expected input[3, 16, 6, 6] to have 32 channels, but got 16 channels instead

jit:
Failed running call_function <built-in method conv_transpose2d of type object at 0x740e29d96ec0>(*(FakeTensor(..., device='cuda:0', size=(3, 16, 6, 6)), Parameter(FakeTensor(..., device='cuda:0', size=(32, 64, 3, 3), requires_grad=True)), Parameter(FakeTensor(..., device='cuda:0', size=(64,), requires_grad=True)), (2, 2), (0, 0), (0, 0), 1, (1, 1)), **{}):
Given transposed=1, weight of size [32, 64, 3, 3], expected input[3, 16, 6, 6] to have 32 channels, but got 16 channels instead

from user code:
   File "<string>", line 24, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 1162, in forward
    return F.conv_transpose2d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''