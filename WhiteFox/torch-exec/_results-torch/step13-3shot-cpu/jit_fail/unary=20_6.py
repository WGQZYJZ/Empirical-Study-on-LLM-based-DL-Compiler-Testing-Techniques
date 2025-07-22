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
        self.conv_t = torch.nn.ConvTranspose2d(1, 1, kernel_size=21, stride=(1, 1), padding=(4, 23))

    def forward(self, v):
        v0 = v
        v1 = self.conv_t(v0)
        v2 = torch.sigmoid(v1)
        return v2



func = Model().to('cpu')


v = torch.randn(1, 2, 24, 5)

test_inputs = [v]

# JIT_FAIL
'''
direct:
Given transposed=1, weight of size [1, 1, 21, 21], expected input[1, 2, 24, 5] to have 1 channels, but got 2 channels instead

jit:
Failed running call_function <built-in method conv_transpose2d of type object at 0x76fcc3196ec0>(*(FakeTensor(..., size=(1, 2, 24, 5)), Parameter(FakeTensor(..., size=(1, 1, 21, 21), requires_grad=True)), Parameter(FakeTensor(..., size=(1,), requires_grad=True)), (1, 1), (4, 23), (0, 0), 1, (1, 1)), **{}):
Given transposed=1, weight of size [1, 1, 21, 21], expected input[1, 2, 24, 5] to have 1 channels, but got 2 channels instead

from user code:
   File "<string>", line 21, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 1162, in forward
    return F.conv_transpose2d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''