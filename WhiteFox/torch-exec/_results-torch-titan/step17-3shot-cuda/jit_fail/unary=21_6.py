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
        self.conv = torch.nn.Conv3d(5, 6, 7, stride=[(- 16383), (- 12345), (- 3141)], dilation=[(- 843), (- 5), 1234567], padding=[314, 23, 78])
        self.relu = torch.nn.ReLU()
        self.bn = torch.nn.BatchNorm2d(64)

    def forward(self, x):
        v1 = self.conv(x)
        v2 = self.relu(v1)
        v3 = self.bn(v2)
        return torch.tanh(v3)




func = ModelTanh().to('cuda')



t = torch.randn(1, 5, 17, 23, 45)


test_inputs = [t]

# JIT_FAIL
'''
direct:
non-positive stride is not supported

jit:
Failed running call_module L__self___conv(*(FakeTensor(..., device='cuda:0', size=(1, 5, 17, 23, 45)),), **{}):
non-positive stride is not supported

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''