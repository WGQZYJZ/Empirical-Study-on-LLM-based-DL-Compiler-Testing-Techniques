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

    def __init__(self, negative_slope):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose2d(63, 75, 1, stride=1, padding=1)
        self.negative_slope = negative_slope

    def forward(self, x):
        v1 = self.conv_transpose(x)
        v2 = v1 > 0
        v3 = v1 * self.negative_slope
        v4 = torch.where(v2, v1, v3).permute(0, 1, 4, 2, 3)
        return v4.reshape(36339).permute(1, 0)


negative_slope = 0.5

func = Model(negative_slope).to('cpu')


x = torch.randn(1, 223, 1, 1)

test_inputs = [x]

# JIT_FAIL
'''
direct:
Given transposed=1, weight of size [63, 75, 1, 1], expected input[1, 223, 1, 1] to have 63 channels, but got 223 channels instead

jit:
Failed running call_function <built-in method conv_transpose2d of type object at 0x72e17f596ec0>(*(FakeTensor(..., size=(1, 223, 1, 1)), Parameter(FakeTensor(..., size=(63, 75, 1, 1), requires_grad=True)), Parameter(FakeTensor(..., size=(75,), requires_grad=True)), (1, 1), (1, 1), (0, 0), 1, (1, 1)), **{}):
Given transposed=1, weight of size [63, 75, 1, 1], expected input[1, 223, 1, 1] to have 63 channels, but got 223 channels instead

from user code:
   File "<string>", line 21, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 1162, in forward
    return F.conv_transpose2d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''