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
        self.conv_t = torch.nn.ConvTranspose2d(1, 11, kernel_size=[4, 5], stride=[3, 2], padding=[2, 1], bias=False)

    def forward(self, x5):
        v1 = self.conv_t(x5)
        v2 = v1 > 0
        v3 = v1 * -0.1
        v4 = torch.where(v2, v1, v3)
        return v4



func = Model().to('cpu')


x5 = torch.randn(23, 1, 10)

test_inputs = [x5]

# JIT_FAIL
'''
direct:
Given transposed=1, weight of size [1, 11, 4, 5], expected input[1, 23, 1, 10] to have 1 channels, but got 23 channels instead

jit:
Failed running call_function <built-in method conv_transpose2d of type object at 0x7e2f3ff96ec0>(*(FakeTensor(..., size=(23, 1, 10)), Parameter(FakeTensor(..., size=(1, 11, 4, 5), requires_grad=True)), None, (3, 2), (2, 1), (0, 0), 1, (1, 1)), **{}):
Given transposed=1, weight of size [1, 11, 4, 5], expected input[1, 23, 1, 10] to have 1 channels, but got 23 channels instead

from user code:
   File "<string>", line 20, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 1162, in forward
    return F.conv_transpose2d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''