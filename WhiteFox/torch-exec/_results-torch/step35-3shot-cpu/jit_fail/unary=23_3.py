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
        self.conv = torch.nn.Conv2d(96, 192, kernel_size=(1, 3), stride=(1, 1), padding=(0, 1))
        self.conv_transpose = torch.nn.ConvTranspose2d(192, 128, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))

    def forward(self, x1):
        v1 = self.conv_transpose(x1)
        v2 = torch.tanh(v1)
        return v2



func = Model().to('cpu')


x1 = torch.randn(1, 96, 35, 192)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given transposed=1, weight of size [192, 128, 3, 3], expected input[1, 96, 35, 192] to have 192 channels, but got 96 channels instead

jit:
Failed running call_function <built-in method conv_transpose2d of type object at 0x7cab48b96ec0>(*(FakeTensor(..., size=(1, 96, 35, 192)), Parameter(FakeTensor(..., size=(192, 128, 3, 3), requires_grad=True)), Parameter(FakeTensor(..., size=(128,), requires_grad=True)), (1, 1), (1, 1), (0, 0), 1, (1, 1)), **{}):
Given transposed=1, weight of size [192, 128, 3, 3], expected input[1, 96, 35, 192] to have 192 channels, but got 96 channels instead

from user code:
   File "<string>", line 21, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 1162, in forward
    return F.conv_transpose2d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''