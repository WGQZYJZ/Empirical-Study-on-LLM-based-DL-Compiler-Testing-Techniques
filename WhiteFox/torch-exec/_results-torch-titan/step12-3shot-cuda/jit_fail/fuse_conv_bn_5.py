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
        self.conv0 = torch.nn.Conv2d(4, 8, 3)
        self.bn0 = torch.nn.BatchNorm2d(8)

    def forward(self, x2):
        return self.conv0(self.bn0(x2))




func = Model().to('cuda')



x2 = torch.randn(1, 4, 4, 4)


test_inputs = [x2]

# JIT_FAIL
'''
direct:
running_mean should contain 4 elements not 8

jit:
Failed running call_module L__self___bn0(*(FakeTensor(..., device='cuda:0', size=(1, 4, 4, 4)),), **{}):
running_mean should contain 4 elements not 8

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''