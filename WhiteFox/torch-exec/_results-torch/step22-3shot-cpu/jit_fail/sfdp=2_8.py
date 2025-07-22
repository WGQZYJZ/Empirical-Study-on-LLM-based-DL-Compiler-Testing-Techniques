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

    def forward(self, x1, x2):
        v1 = F.conv2d(x1, x2, None)
        inv_scale_factor = 1 / (x1.shape[-1] * x1.shape[-2] + x2.shape[-1] * x2.shape[-2])
        v2 = v1.div(inv_scale_factor)
        v3 = F.softmax(v2, dim=-1)
        v4 = F.dropout(v3, 0.5, True, False)
        v5 = F.conv2d(v4, x2, None)
        return v5


func = Model().to('cpu')


x1 = torch.randn(1, 3, 64, 64)

x2 = torch.randn(1, 3, 64, 64)

test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [1, 3, 64, 64], expected input[1, 1, 1, 1] to have 3 channels, but got 1 channels instead

jit:
Failed running call_function <built-in method conv2d of type object at 0x7bf95f996ec0>(*(FakeTensor(..., size=(1, 1, 1, 1)), FakeTensor(..., size=(1, 3, 64, 64)), None), **{}):
Given groups=1, weight of size [1, 3, 64, 64], expected input[1, 1, 1, 1] to have 3 channels, but got 1 channels instead

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''