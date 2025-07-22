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
        self.conv_t = torch.nn.ConvTranspose3d(32, 1024, kernel_size=3, stride=2, padding=1)
        self.conv_t = torch.nn.ConvTranspose3d(1024, 512, kernel_size=3, stride=1, padding=1)
        self.conv_t = torch.nn.ConvTranspose3d(512, 512, kernel_size=3, stride=2, padding=1)
        self.conv_t = torch.nn.ConvTranspose3d(512, 256, kernel_size=3, stride=1, padding=1)

    def forward(self, x1):
        v1 = self.conv_t(x1)
        v2 = torch.sigmoid(v1)
        return v2



func = Model().to('cpu')


x1 = torch.randn(1, 32, 64, 64)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given transposed=1, weight of size [512, 256, 3, 3, 3], expected input[1, 1, 32, 64, 64] to have 512 channels, but got 1 channels instead

jit:
Failed running call_function <built-in method conv_transpose3d of type object at 0x711e9e596ec0>(*(FakeTensor(..., size=(1, 32, 64, 64)), Parameter(FakeTensor(..., size=(512, 256, 3, 3, 3), requires_grad=True)), Parameter(FakeTensor(..., size=(256,), requires_grad=True)), (1, 1, 1), (1, 1, 1), (0, 0, 0), 1, (1, 1, 1)), **{}):
Given transposed=1, weight of size [512, 256, 3, 3, 3], expected input[1, 1, 32, 64, 64] to have 512 channels, but got 1 channels instead

from user code:
   File "<string>", line 23, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 1347, in forward
    return F.conv_transpose3d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''