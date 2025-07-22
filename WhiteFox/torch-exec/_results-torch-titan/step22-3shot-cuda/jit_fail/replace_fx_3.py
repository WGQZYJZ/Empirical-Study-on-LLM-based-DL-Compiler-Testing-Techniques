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



class model(torch.nn.Module):

    def __init__(self):
        super(model, self).__init__()
        self.conv1d1 = torch.nn.Conv1d(in_channels=1, out_channels=3, kernel_size=3, groups=1, bias=True, padding=0)
        self.conv1d2 = torch.nn.Conv1d(in_channels=1, out_channels=3, kernel_size=3, groups=1, bias=True, padding=0)

    def forward(self, x1):
        x2 = self.conv1d1(x1)
        x3 = self.conv1d2(x2)
        x4 = (x3 ** 2)
        x5 = (x4 + x2)
        return x5




func = model().to('cuda')



x1 = torch.randn(1, 1, 100)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [3, 1, 3], expected input[1, 3, 98] to have 1 channels, but got 3 channels instead

jit:
Failed running call_module L__self___conv1d2(*(FakeTensor(..., device='cuda:0', size=(1, 3, 98)),), **{}):
Invalid channel dimensions

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''