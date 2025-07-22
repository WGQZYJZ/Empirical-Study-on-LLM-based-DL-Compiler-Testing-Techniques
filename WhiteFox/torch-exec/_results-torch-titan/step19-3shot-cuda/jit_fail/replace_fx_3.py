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



class A(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(4, 5, kernel_size=5)

    def forward(self, input):
        y = self.conv(input)
        t = input.permute(1, 0, 2, 3)
        z = t.reshape((1, 20))
        x = (y + z)
        out = torch.rand_like(x)
        return out




func = A().to('cuda')



input = torch.randn(1, 3, 256, 256)


test_inputs = [input]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [5, 4, 5, 5], expected input[1, 3, 256, 256] to have 4 channels, but got 3 channels instead

jit:
Failed running call_module L__self___conv(*(FakeTensor(..., device='cuda:0', size=(1, 3, 256, 256)),), **{}):
Given groups=1, weight of size [5, 4, 5, 5], expected input[1, 3, 256, 256] to have 4 channels, but got 3 channels instead

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''