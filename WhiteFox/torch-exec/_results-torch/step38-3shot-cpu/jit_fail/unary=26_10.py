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
        self.conv_t = torch.nn.ConvTranspose2d(1, 3, 3, stride=1, padding=2, bias=False)

    def forward(self, x):
        x1 = self.conv_t(x)
        x2 = x1 > 0
        x3 = x1 * -1.403
        x4 = torch.where(x2, x1, x3)
        return torch.nn.functional.interpolate(x4, scale_factor=[1.0, 1.0])



func = Model().to('cpu')


x = torch.randn(4, 3, 9, 8)

test_inputs = [x]

# JIT_FAIL
'''
direct:
Given transposed=1, weight of size [1, 3, 3, 3], expected input[4, 3, 9, 8] to have 1 channels, but got 3 channels instead

jit:
Failed running call_function <built-in method conv_transpose2d of type object at 0x7a4efd796ec0>(*(FakeTensor(..., size=(4, 3, 9, 8)), Parameter(FakeTensor(..., size=(1, 3, 3, 3), requires_grad=True)), None, (1, 1), (2, 2), (0, 0), 1, (1, 1)), **{}):
Given transposed=1, weight of size [1, 3, 3, 3], expected input[4, 3, 9, 8] to have 1 channels, but got 3 channels instead

from user code:
   File "<string>", line 20, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 1162, in forward
    return F.conv_transpose2d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''