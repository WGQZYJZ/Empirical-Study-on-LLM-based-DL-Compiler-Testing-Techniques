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
        self.conv = torch.nn.Conv2d(3, 128, 1, stride=1, padding=1)

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = (v1 + 3)
        v3 = torch.nn.functional.relu(v2, 0, 6)
        v4 = (v1 * v3)
        v5 = (v4 / 6)
        return v5




func = Model().to('cuda')



x1 = torch.randn(1, 3, 64, 64)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
relu() takes from 1 to 2 positional arguments but 3 were given

jit:
Failed running call_function <function relu at 0x7c6901edfca0>(*(FakeTensor(..., device='cuda:0', size=(1, 128, 66, 66)), 0, 6), **{}):
relu() takes from 1 to 2 positional arguments but 3 were given

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''