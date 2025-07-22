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
        self.conv = torch.nn.Conv1d(2, 4, 3, groups=2)
        c = torch.nn.Conv1d(1, 2, 1)
        bn = torch.nn.BatchNorm1d(2)
        self.layer = torch.nn.Sequential(bn, c)

    def forward(self, x1):
        x1 = self.layer(x1)
        v1 = self.conv(x1)
        return v1




func = Model().to('cuda')



x1 = torch.randn(1, 2, 4)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [2, 1, 1], expected input[1, 2, 4] to have 1 channels, but got 2 channels instead

jit:
Failed running call_module L__self___layer_1(*(FakeTensor(..., device='cuda:0', size=(1, 2, 4)),), **{}):
Invalid channel dimensions

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''