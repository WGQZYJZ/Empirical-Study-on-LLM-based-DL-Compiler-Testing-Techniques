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
        self.conv_transpose_5 = torch.nn.ConvTranspose2d(7338, 1, 7, stride=1, padding=1)

    def forward(self, x1):
        v1 = self.conv_transpose_5(x1)
        v2 = torch.sigmoid(v1)
        v3 = v1 * v2
        return v3



func = Model().to('cpu')


x1 = torch.randn(1, 6638, 1, 3)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given transposed=1, weight of size [7338, 1, 7, 7], expected input[1, 6638, 1, 3] to have 7338 channels, but got 6638 channels instead

jit:
Failed running call_function <built-in method conv_transpose2d of type object at 0x79c264d96ec0>(*(FakeTensor(..., size=(1, s0, 1, s1)), Parameter(FakeTensor(..., size=(7338, 1, 7, 7), requires_grad=True)), Parameter(FakeTensor(..., size=(1,), requires_grad=True)), (1, 1), (1, 1), (0, 0), 1, (1, 1)), **{}):
Given transposed=1, weight of size [7338, 1, 7, 7], expected input[1, s0, 1, s1] to have 7338 channels, but got s0 channels instead

from user code:
   File "<string>", line 20, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 1162, in forward
    return F.conv_transpose2d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''