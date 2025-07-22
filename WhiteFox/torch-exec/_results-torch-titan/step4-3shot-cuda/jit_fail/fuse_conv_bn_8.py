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
        self.c = torch.nn.Conv3d(1, 2, 1)
        self.bn = torch.nn.BatchNorm3d(2)

    def forward(self, x1):
        return self.c(self.bn(x1))




func = Model().to('cuda')



x1 = torch.randn(4, 1, 4, 4, 4)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
running_mean should contain 1 elements not 2

jit:
Failed running call_module L__self___bn(*(FakeTensor(..., device='cuda:0', size=(4, 1, 4, 4, 4)),), **{}):
running_mean should contain 1 elements not 2

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''