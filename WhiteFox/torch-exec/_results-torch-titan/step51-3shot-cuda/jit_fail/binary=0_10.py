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
        self.conv = torch.nn.Conv2d(64, 256, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))

    def forward(self, x1, kernel, other, group=1):
        v1 = self.conv(x1)
        v2 = (v1 + other)
        return v2




func = Model().to('cuda')



x1 = torch.randn(1, 3, 64, 64)



kernel = torch.randn(3, 3)

other = 1

test_inputs = [x1, kernel, other]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [256, 64, 3, 3], expected input[1, 3, 64, 64] to have 64 channels, but got 3 channels instead

jit:
Failed running call_module L__self___conv(*(FakeTensor(..., device='cuda:0', size=(1, 3, 64, 64)),), **{}):
Given groups=1, weight of size [256, 64, 3, 3], expected input[1, 3, 64, 64] to have 64 channels, but got 3 channels instead

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''