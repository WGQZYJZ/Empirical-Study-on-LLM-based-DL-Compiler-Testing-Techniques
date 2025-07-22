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
        self.conv = torch.nn.Conv2d(2, 1, 3, 1, 0)
        self.bn = torch.nn.BatchNorm2d(2)

    def forward(self, x):
        return torch.nn.ReLU((self.bn(self.conv(x)) + self.bn(self.conv(x))))




func = Model().to('cuda')



x = torch.randn(1, 2, 6, 6)


test_inputs = [x]

# JIT_FAIL
'''
direct:
running_mean should contain 1 elements not 2

jit:
Failed running call_module L__self___bn(*(FakeTensor(..., device='cuda:0', size=(1, 1, 4, 4)),), **{}):
running_mean should contain 1 elements not 2

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''