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
        self.convtranspose1 = torch.nn.ConvTranspose1d(64, 512, kernel_size=3, stride=1, padding=1)
        self.convtranspose2 = torch.nn.ConvTranspose2d(64, 512, 3, stride=1, padding=1)

    def forward(self, x1):
        v1 = self.convtranspose1(x1)
        v2 = self.convtranspose2(x1)
        v3 = torch.mean(torch.reshape(v1, (-1, 512, 1)))
        v4 = torch.sigmoid(v3)
        return v4 + v2



func = Model().to('cpu')


x1 = torch.randn(1, 64, 64)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given transposed=1, weight of size [64, 512, 3, 3], expected input[1, 1, 64, 64] to have 64 channels, but got 1 channels instead

jit:
Failed running call_function <built-in method conv_transpose2d of type object at 0x7e6917996ec0>(*(FakeTensor(..., size=(1, 64, 64)), Parameter(FakeTensor(..., size=(64, 512, 3, 3), requires_grad=True)), Parameter(FakeTensor(..., size=(512,), requires_grad=True)), (1, 1), (1, 1), (0, 0), 1, (1, 1)), **{}):
Given transposed=1, weight of size [64, 512, 3, 3], expected input[1, 1, 64, 64] to have 64 channels, but got 1 channels instead

from user code:
   File "<string>", line 22, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 1162, in forward
    return F.conv_transpose2d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''