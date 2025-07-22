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

    def forward(self, x1):
        v1 = torch.nn.functional.conv_transpose2d(input=x1, weight=torch.empty([32, 3, 5, 5]), bias=None, stride=(2, 2), padding=(0, 1))
        v2 = v1 + 3
        v3 = torch.clamp_min(v2, 0)
        v4 = torch.clamp_max(v3, 6)
        v5 = v4 / 6
        return v5



func = Model().to('cpu')


x1 = torch.randn(1, 3, 64, 64)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given transposed=1, weight of size [32, 3, 5, 5], expected input[1, 3, 64, 64] to have 32 channels, but got 3 channels instead

jit:
Failed running call_function <built-in method conv_transpose2d of type object at 0x7b8ea1596ec0>(*(), **{'input': FakeTensor(..., size=(1, 3, 64, 64)), 'weight': FakeTensor(..., size=(32, 3, 5, 5)), 'bias': None, 'stride': (2, 2), 'padding': (0, 1)}):
Given transposed=1, weight of size [32, 3, 5, 5], expected input[1, 3, 64, 64] to have 32 channels, but got 3 channels instead

from user code:
   File "<string>", line 19, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''