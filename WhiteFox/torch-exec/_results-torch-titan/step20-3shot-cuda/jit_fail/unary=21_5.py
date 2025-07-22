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



class ModelTanh(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(6, 3, (16, 16), stride=(16, 16), bias=False)

    def forward(self, x0):
        v1 = self.conv(x0)
        v2 = torch.tanh(v1)
        return v2




func = ModelTanh().to('cuda')



x0 = torch.randn(1, 1, 32, 32)


test_inputs = [x0]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [3, 6, 16, 16], expected input[1, 1, 32, 32] to have 6 channels, but got 1 channels instead

jit:
Failed running call_module L__self___conv(*(FakeTensor(..., device='cuda:0', size=(1, 1, 32, 32)),), **{}):
Given groups=1, weight of size [3, 6, 16, 16], expected input[1, 1, 32, 32] to have 6 channels, but got 1 channels instead

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''