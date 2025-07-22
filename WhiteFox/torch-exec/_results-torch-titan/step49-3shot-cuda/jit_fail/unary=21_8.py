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

    def __init__(self, m, s):
        super().__init__()
        self.conv = torch.nn.Conv2d(m, s, 1, stride=1, padding=1)

    def forward(self, x2):
        y2 = self.conv(x2)
        t2 = torch.tanh(y2)
        return t2



m = 1
s = 1

func = ModelTanh(m, s).to('cuda')



x2 = torch.randn(1, 3, 64, 64)


test_inputs = [x2]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [1, 1, 1, 1], expected input[1, 3, 64, 64] to have 1 channels, but got 3 channels instead

jit:
Failed running call_module L__self___conv(*(FakeTensor(..., device='cuda:0', size=(1, 3, 64, 64)),), **{}):
Given groups=1, weight of size [1, 1, 1, 1], expected input[1, 3, 64, 64] to have 1 channels, but got 3 channels instead

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''