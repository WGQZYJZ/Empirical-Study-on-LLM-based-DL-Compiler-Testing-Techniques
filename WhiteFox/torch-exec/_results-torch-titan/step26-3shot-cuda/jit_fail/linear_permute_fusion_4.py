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
        self.conv = torch.nn.Conv2d(2, 2, 3)

    def forward(self, x1):
        x2 = x1[:, :, 0, :]
        y = self.conv(x2)
        v1 = torch.nn.functional.linear(y, self.conv.weight, self.conv.bias)
        v2 = v1.permute(3, 1, 0, 2)
        return v1




func = Model().to('cuda')



x1 = torch.randn(1, 2, 5, 5)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [2, 2, 3, 3], expected input[1, 1, 2, 5] to have 2 channels, but got 1 channels instead

jit:
Failed running call_module L__self___conv(*(FakeTensor(..., device='cuda:0', size=(1, 2, 5)),), **{}):
Given groups=1, weight of size [2, 2, 3, 3], expected input[1, 1, 2, 5] to have 2 channels, but got 1 channels instead

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''