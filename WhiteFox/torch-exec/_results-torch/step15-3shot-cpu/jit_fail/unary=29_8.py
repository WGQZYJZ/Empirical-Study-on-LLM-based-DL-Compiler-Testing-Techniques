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

    def __init__(self, min_value=0, max_value=0):
        super().__init__()
        self.conv = torch.nn.Conv2d(256, 32, 1, stride=1, padding=0)
        self.conv_transpose = torch.nn.ConvTranspose2d(32, 16, 75, stride=53, padding=0)
        self.min_value = min_value
        self.max_value = max_value

    def forward(self, x1):
        v1 = self.conv_transpose(x1)
        v2 = torch.clamp_min(v1, self.min_value)
        v3 = torch.clamp_max(v2, self.max_value)
        v4 = v3
        return v4



func = Model().to('cpu')


x1 = torch.randn(1, 256, 1, 1)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given transposed=1, weight of size [32, 16, 75, 75], expected input[1, 256, 1, 1] to have 32 channels, but got 256 channels instead

jit:
Failed running call_function <built-in method conv_transpose2d of type object at 0x74cecb196ec0>(*(FakeTensor(..., size=(1, 256, 1, 1)), Parameter(FakeTensor(..., size=(32, 16, 75, 75), requires_grad=True)), Parameter(FakeTensor(..., size=(16,), requires_grad=True)), (53, 53), (0, 0), (0, 0), 1, (1, 1)), **{}):
Given transposed=1, weight of size [32, 16, 75, 75], expected input[1, 256, 1, 1] to have 32 channels, but got 256 channels instead

from user code:
   File "<string>", line 23, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 1162, in forward
    return F.conv_transpose2d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''