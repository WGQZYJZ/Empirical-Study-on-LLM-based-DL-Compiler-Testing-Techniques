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
        self.conv1 = torch.nn.Conv1d(3, 1, 1, stride=1, padding=0)
        self.bn1 = torch.nn.BatchNorm1d(1)
        self.conv2 = torch.nn.Conv1d(1, 4, 1, stride=1, padding=0)
        self.bn2 = torch.nn.BatchNorm1d(4)

    def forward(self, x):
        negative_slope = 0.01164564
        v1 = self.conv1(x)
        v2 = self.bn1(v1)
        v3 = (v2 > 0)
        v4 = (v2 * negative_slope)
        v5 = torch.where(v3, v2, v4)
        v6 = self.conv2(v5)
        v7 = self.bn2(v6)
        return v7




func = Model().to('cuda')



x1 = torch.randn(5, 1, 800)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [1, 3, 1], expected input[5, 1, 800] to have 3 channels, but got 1 channels instead

jit:
Failed running call_module L__self___conv1(*(FakeTensor(..., device='cuda:0', size=(5, 1, 800)),), **{}):
Invalid channel dimensions

from user code:
   File "<string>", line 26, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''