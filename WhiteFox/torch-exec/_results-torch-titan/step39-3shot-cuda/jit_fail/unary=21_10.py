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
        self.conv = torch.nn.Conv2d(10, 50, 2, padding=0, groups=2, bias=False)

    def forward(self, x0):
        v1 = self.conv(x0)
        v2 = torch.tanh(v1)
        return v2




func = ModelTanh().to('cuda')



x0 = torch.randn(10, 1, 36, 24)


test_inputs = [x0]

# JIT_FAIL
'''
direct:
Given groups=2, weight of size [50, 5, 2, 2], expected input[10, 1, 36, 24] to have 10 channels, but got 1 channels instead

jit:
Failed running call_module L__self___conv(*(FakeTensor(..., device='cuda:0', size=(10, 1, 36, 24)),), **{}):
Given groups=2, weight of size [50, 5, 2, 2], expected input[10, 1, 36, 24] to have 10 channels, but got 1 channels instead

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''