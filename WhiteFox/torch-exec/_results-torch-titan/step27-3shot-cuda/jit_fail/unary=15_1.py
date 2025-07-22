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
        self.conv = torch.nn.Conv2d(3, 3, 2, stride=2, padding=2)

    def forward(self, x1):
        v1 = self.conv(x1)
        return v1




func = Model().to('cuda')



x1 = torch.randn(4, 1, 16, 16)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [3, 3, 2, 2], expected input[4, 1, 16, 16] to have 3 channels, but got 1 channels instead

jit:
Failed running call_module L__self___conv(*(FakeTensor(..., device='cuda:0', size=(4, 1, 16, 16)),), **{}):
Given groups=1, weight of size [3, 3, 2, 2], expected input[4, 1, 16, 16] to have 3 channels, but got 1 channels instead

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''