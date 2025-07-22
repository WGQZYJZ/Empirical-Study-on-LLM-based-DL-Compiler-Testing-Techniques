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



class Conv2D(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(1, 5, 3, stride=1, padding=1)

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.relu(v1)
        v3 = (torch.relu(v1) * torch.relu(v1))
        v4 = torch.nn.functional.interpolate(v3, scale_factor=None)
        v5 = (torch.relu(v1) * 0.6)
        v7 = ((torch.nn.functional.sigmoid(v4) * 123) - 456)
        v10 = (torch.tanh((v5 + v7)) + 1)
        v11 = (torch.tanh(v2) + v10)
        return v11




func = Conv2D().to('cuda')



x1 = torch.randn(1, 1, 223, 319)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
either size or scale_factor should be defined

jit:
Failed running call_function <function interpolate at 0x7792905f7430>(*(FakeTensor(..., device='cuda:0', size=(1, 5, 223, 319)),), **{'scale_factor': None}):
either size or scale_factor should be defined

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''