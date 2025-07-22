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
        self.c1 = torch.nn.Conv2d(3, 10, 1)
        self.c2 = torch.nn.Conv2d(3, 10, 1)
        self.b = torch.nn.BatchNorm2d(3)

    def forward(self, x):
        out_1 = self.c1(x)
        out_2 = self.c2(x)
        out = torch.cat([out_1, out_2], 1)
        out = self.b(out)
        return out




func = Model().to('cuda')



x = torch.randn(1, 3, 1, 1)


test_inputs = [x]

# JIT_FAIL
'''
direct:
running_mean should contain 20 elements not 3

jit:
Failed running call_module L__self___b(*(FakeTensor(..., device='cuda:0', size=(1, 20, 1, 1)),), **{}):
running_mean should contain 20 elements not 3

from user code:
   File "<string>", line 27, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''